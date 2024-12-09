# Interpretador adaptativo 3.13

Diagrama: https://excalidraw.com/#json=USjGJ0H1kRrb9SbtpjLPf,iTJ2LmcsXJENaq4ZGsSYhg

Questionamentos do dia:
	- Quando o interpretador faz a troca do tier 1 pro tier 2?
		- Baseado em que?
	- Onde o JUMP é adicionado?
	- Existe uma forma de ver as micro-ops? (mesmo no gdb)
	- cpython/Python/tier2_engine.md (olhar depois com calma)
	
---

O intepretador conta com algumas diferenças na versão 3.13:

1. A interpretação de bytecodes agora é divida em tiers
2. Os tiers mudam o executador de bytecode
3. Por padrão o executador (`co_executors`) é `NULL`
  - O executador padrão executa o código gerado pela DSL 3.12
4. O processo de quickening foi modificado
5. O executador padrão faz otimizações de tier 1
   - por tier 1 entenda o mesmo processo adaptativo das versões 3.11 e 3.12
6. Em algum momento (que ainda não entendi) a otimização vai para tier 2
   - O `co->co_executors` recebe um executador
	 - Se `--enable-experimental-jit=interpreter` foi setada na compilação o executador de tier 2 é o JIT
	 - Caso contrário, existe um executador padrão para tier 2 sem JIT
7. Sobre o tier 2
   - O tier 2 conta com mais opcodes
   - os opcodes do tier 2 são micro-ops
   - As operações de micro-ops são instruções melhoradas para compilação.
   
---
8. Por existirem dois tiers, o código de todos os bytecodes é mantido em uma DSL em `Python/bytecodes.c`
   - Existe uma ferramenta em `Tools/cases_generator/` que transforma esse único arquivo em dois:
	 - `tierN_generator.py` que gera o código para o tier N em `Python/generated_cases.c.h`
	 - `optimizer_generator.py` que gera `Python/optimizer_cases.c.h`
	 - algumas explicações sobre a troca dos tiers estão em Python/tier2_engine.md
---

O frame é montado, o code agora tem o `co_executors` que é inicializado como `NULL`.

Enquanto for `NULL` ele está no tier 1.


tier 0: Quickning -> SuperInstructions / Cache (`co_executors==NULL`)
tier 1: Adapative {HOT}
	????????? {hotness}
	co_executors != NULL [optimizer]


O código já é compilado com instruções mais rápidas (like load_fast_load_fast) e com o sistema de inline cache inicializado!

Nas chamadas o sistema de especialização é chamado a toda execução para o calculo do cache:

```c
//specialize.c
void
_PyCode_Quicken(PyCodeObject *code)
{
    #if ENABLE_SPECIALIZATION
    int opcode = 0;
    _Py_CODEUNIT *instructions = _PyCode_CODE(code);
    for (int i = 0; i < Py_SIZE(code); i++) {
        opcode = _Py_GetBaseOpcode(code, i);  // pega os códigos em Include/opcodes_ids.h
        assert(opcode < MIN_INSTRUMENTED_OPCODE); // garante não está acontecendo instrumentação
        int caches = _PyOpcode_Caches[opcode]; // Include/internal/pycore_opcode_metadata.h (1598)
        if (caches) {
            // The initial value depends on the opcode
            switch (opcode) {
				// ...
                default:
                    instructions[i + 1].counter = adaptive_counter_warmup();
                    break;
            }
            i += caches;
        }
    }
    #endif /* ENABLE_SPECIALIZATION */
}
```
