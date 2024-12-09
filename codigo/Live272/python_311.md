# Interpretador adaptativo 3.11

## Funções

Nessa investigação usaremos duas funções extremamente simples.

Uma função de soma:
```python
def add(x, y): return x + y
```

O bytecode da função de soma usando dis.dis:

```python
>>> dis(add)
  1           0 RESUME                   0
              2 LOAD_FAST                0 (x)
              4 LOAD_FAST                1 (y)
              6 BINARY_OP                0 (+)
             10 RETURN_VALUE
```

E uma função que faz uma chamada de nomes ao namespace builtin:

```python
def get_builtin(): return str(42)
```

E seu bytecode:

```python
>>> dis(get_builtin)
  1           0 RESUME                   0
              2 LOAD_GLOBAL              1 (NULL + str)
             14 LOAD_CONST               1 (42)
             16 PRECALL                  1
             20 CALL                     1
             30 RETURN_VALUE
```

## O Code

O code é inicializado com um contador de chamadas em `frame->co_warmup`:

```c
//codeobject.c
co->co_warmup = QUICKENING_INITIAL_WARMUP_VALUE; // 339
```

https://github.com/python/cpython/blob/795f2597a4be988e2bb19b69ff9958e981cb894e/Objects/codeobject.c#L289-L290

O valor de `QUICKENING_INITIAL_WARMUP_VALUE` é -8

```c
// pycore_code.h
#define QUICKENING_WARMUP_DELAY 8 // 95

/* We want to compare to zero for efficiency, so we offset values accordingly */
#define QUICKENING_INITIAL_WARMUP_VALUE (-QUICKENING_WARMUP_DELAY)
```


## O eval p1

Uma novidade da versão 3.11 é a 'opcode' `RESUME`.

Uma das funções do `RESUME` é adicionar `+1` ao valor de `co_warmup` via `_PyCode_Warmup`:

```c
// ceval.c
        TARGET(RESUME) { // 1770
            _PyCode_Warmup(frame->f_code);
            JUMP_TO_INSTRUCTION(RESUME_QUICK);
        }
        TARGET(RESUME_QUICK) {
            PREDICTED(RESUME_QUICK);
            assert(tstate->cframe == &cframe);
            assert(frame == cframe.current_frame);
            if (_Py_atomic_load_relaxed_int32(eval_breaker) && oparg < 2) {
                goto handle_eval_breaker;
            }
            DISPATCH();
        }
```

A função `_PyCode_Warmup` incrementa o valor de `co_warmup` em 1. Caso o valor seja igual a 0, o quicken:

```c
//python_code.h
static inline void // 102
_PyCode_Warmup(PyCodeObject *code)
{
    if (code->co_warmup != 0) {
        code->co_warmup++;
        if (code->co_warmup == 0) {
            _PyCode_Quicken(code);
        }
    }
}
```

A função `_PyCode_Quicken` olha as operações do bytecode e busca por operações que podem "performar melhor" durante a avalização do bytecode.


```c
//specialize.c
void  // 259
_PyCode_Quicken(PyCodeObject *code)
{
    // ...
    for (int i = 0; i < Py_SIZE(code); i++) {
        int opcode = _Py_OPCODE(instructions[i]);
        uint8_t adaptive_opcode = _PyOpcode_Adaptive[opcode];
        if (adaptive_opcode) {
            _Py_SET_OPCODE(instructions[i], adaptive_opcode);
            // Make sure the adaptive counter is zero:
            assert(instructions[i + 1] == 0);
            previous_opcode = -1;
            i += _PyOpcode_Caches[opcode];
        }
        else {
		// ...
                case RESUME:
                    _Py_SET_OPCODE(instructions[i], RESUME_QUICK);
                    break;
                case LOAD_FAST:
                    switch(previous_opcode) {
                        case LOAD_FAST:
                            _Py_SET_OPCODE(instructions[i - 1],
                                           LOAD_FAST__LOAD_FAST);
                            break;
                        case STORE_FAST:
                            _Py_SET_OPCODE(instructions[i - 1],
                                           STORE_FAST__LOAD_FAST);
                            break;
                        case LOAD_CONST:
                            _Py_SET_OPCODE(instructions[i - 1],
                                           LOAD_CONST__LOAD_FAST);
                            break;
                    }
                    break;
```

O exemplo de código selecionado de `_PyCode_Quicken` mostra que quando duas instruções de `LOAD_FAST` forem feitas de forma consecutiva, a operação será substituída por uma única operação `LOAD_FAST__LOAD_FAST`. Chamamos essa operação que faz duas operações de **superinstructions**.

Assim como serão buscadas opcodes que podem ser adaptados `adaptive_opcode = _PyOpcode_Adaptive[opcode];`



### Após a especialização

Caso o código seja detectado como "quente" [warm] a primeira operação do bytecode `RESUME` será substituída por `RESUME_QUICK`. A operação que normalmente é chamada após a adição de `+1` em `co_warmup` pelo `RESUME`.

Uma outra coisa interessante é que durante o `Quicken`, todas as operações do bytecode serão investigadas para ver se existe uma versão adaptativa em `_PyOpcode_Adaptive`:

```c
// specialize.c
uint8_t _PyOpcode_Adaptive[256] = { // 20
    [LOAD_ATTR] = LOAD_ATTR_ADAPTIVE,
    [LOAD_GLOBAL] = LOAD_GLOBAL_ADAPTIVE,
    [LOAD_METHOD] = LOAD_METHOD_ADAPTIVE,
    [BINARY_SUBSCR] = BINARY_SUBSCR_ADAPTIVE,
    [STORE_SUBSCR] = STORE_SUBSCR_ADAPTIVE,
    [CALL] = CALL_ADAPTIVE,
    [PRECALL] = PRECALL_ADAPTIVE,
    [STORE_ATTR] = STORE_ATTR_ADAPTIVE,
    [BINARY_OP] = BINARY_OP_ADAPTIVE,
    [COMPARE_OP] = COMPARE_OP_ADAPTIVE,
    [UNPACK_SEQUENCE] = UNPACK_SEQUENCE_ADAPTIVE,
};
```

Para as instruções que tiverem operações adaptativas, serão substituídas.

## Adaptação

Após o quickening, o bytecode da função de soma deve se parecer com isso:

```python
  1           0 RESUME_QUICK                 0
              2 LOAD_FAST__LOAD_FAST         0 (x)
              4 LOAD_FAST                    1 (y)
			  6 BINARY_OP_ADAPTIVE           0 (+)
             10 RETURN_VALUE
```

Temos que lembrar, porém, que estamos em uma chamada de avaliação em `ceval`. O que quer dizer que a operação de `RESUME` já foi executada e as operações seguintes a ela serão executadas. Como:

```python
              2 LOAD_FAST__LOAD_FAST         0 (x)
              4 LOAD_FAST                    1 (y)
			  6 BINARY_OP_ADAPTIVE           0 (+)
             10 RETURN_VALUE
```

As operações serão executadas normalmente com os `targets` do switch da avaliação. O caso especial é para operações que tem o final `*_ADAPTIVE`.

Durante a avaliação serão transformadas em outras operações. Por exemplo `BINARY_OP_ADAPTIVE`:

```c
// ceval.c
        TARGET(BINARY_OP_ADAPTIVE) { // 5559
            assert(cframe.use_tracing == 0);
            _PyBinaryOpCache *cache = (_PyBinaryOpCache *)next_instr;
            if (ADAPTIVE_COUNTER_IS_ZERO(cache)) {
                PyObject *lhs = SECOND();
                PyObject *rhs = TOP();
                next_instr--;
                _Py_Specialize_BinaryOp(lhs, rhs, next_instr, oparg, &GETLOCAL(0));
                DISPATCH_SAME_OPARG();
            }
            else {
                STAT_INC(BINARY_OP, deferred);
                DECREMENT_ADAPTIVE_COUNTER(cache);
                JUMP_TO_INSTRUCTION(BINARY_OP);
            }
        }
```

Nessa etapa de execução `BINARY_OP_ADAPTIVE`, será feita uma chamada para `_Py_Specialize_BinaryOp`:

```c
// specialize.c
void
_Py_Specialize_BinaryOp(PyObject *lhs, PyObject *rhs, _Py_CODEUNIT *instr,
                        int oparg, PyObject **locals)
{ // 1805
// ...
        case NB_INPLACE_ADD: // 1810
            if (!Py_IS_TYPE(lhs, Py_TYPE(rhs))) {
                break;
            }
			// ...
            if (PyLong_CheckExact(lhs)) {
                _Py_SET_OPCODE(*instr, BINARY_OP_ADD_INT);
                goto success;
            }
            if (PyFloat_CheckExact(lhs)) {
                _Py_SET_OPCODE(*instr, BINARY_OP_ADD_FLOAT);
                goto success;
            }
            break;
// ...
```

Os dois valores da operação binária serão extraídos e seus tipos serão validados. Se os tipos forem iguais, a operação será especializada em um novo opcode. Por exemplo:

- Dois inteiros: `BINARY_OP_ADD_INT`
- Dois floats: `BINARY_OP_ADD_FLOAT`
- Duas strings: `BINARY_OP_ADD_UNICODE`


## Cache

O cache é executado nas operações adaptativas. Cada operação tem uma struct de cache.

No caso da operação `BINARY_OP_ADAPTIVE`. Ele iniciará a struct `_PyBinaryOpCache`:

```c
// pycore_code.h
typedef struct {  //27
    _Py_CODEUNIT counter;
} _PyBinaryOpCache;
```

O cache vira uma instrução do bytecode:

```python
>>> dis(add, show_caches=True, adaptive=True)
  1           0 RESUME                   0
              2 LOAD_FAST                0 (x)
              4 LOAD_FAST                1 (y)
              6 BINARY_OP                0 (+)
              8 CACHE                    0
             10 RETURN_VALUE
```

Para operações como `BINARY_OP_ADAPTIVE`, que a struct tem somente um valor `counter`, o cache contabiliza somente essa operação.

Após o código esquentar, podemos ver a variável `counter` no cache:

```python
>>> [add(1, 1) for _ in range(8)]
[2, 2, 2, 2, 2, 2, 2, 2]

>>> dis(add, show_caches=True, adaptive=True)
  1           0 RESUME_QUICK             0
              2 LOAD_FAST__LOAD_FAST     0 (x)
              4 LOAD_FAST                1 (y)
              6 BINARY_OP_ADD_INT        0 (+)
              8 CACHE                    0 (counter: 53)
             10 RETURN_VALUE
```

### Counter

Cada instrução adaptativa tem um valor diferente de cache. Os caches são iniciados na operação `*_ADAPTIVE`. E pra cada chamada em que a operação especializada "errar" um valor é decrementado do contador.

Tanto o valor inicial do contador quanto o valor decrementado é referente ao opcode adaptado.

### A função que pega valores do namespace

A especialização de `LOAD_GLOBAL` no caso da função que pega um builtin é `LOAD_GLOBAL_BUILTIN` e esse opcode tem um cache bem robusto:

```c
typedef struct {
    _Py_CODEUNIT counter;
    _Py_CODEUNIT index;
    _Py_CODEUNIT module_keys_version[2];
    _Py_CODEUNIT builtin_keys_version;
} _PyLoadGlobalCache;
```

Onde o contador tem a função de readaptar o código. Mas, existem valores como `index`, `module_keys_version` e `builtin_keys_version`.

Nesse caso em específico será feita uma espécie de "hash" do namespace global e dos builtins e eles serão armazenados em `module_keys_version` e `builtin_keys_version`. O valor do `index` é responsável por saber a posição em que o `builtin` que pedimos está nessa versão específica do namespace.

O bytecode final tem esse aparência por conta da grande quantidade de cache:

```python
>>> dis(get_builtin, adaptive=True, show_caches=True)
  1           0 RESUME_QUICK             0
              2 LOAD_GLOBAL_BUILTIN      1 (NULL + str)
              4 CACHE                    0 (counter: 53)
              6 CACHE                    0 (index: 75)
              8 CACHE                    0 (module_keys_version: 76)
             10 CACHE                    0
             12 CACHE                    0 (builtin_keys_version: 66)
# ...
```

Onde todos os valores da struct são contemplados no opcode de `CACHE`.

## O eval p2

Um caso interessante de pensar é o que acontece quando o mesmo bloco de código é chamado com valores que não foram otimizados pelo bytecode.

### Validações em opcodes

Vamos usar o caso do opcode de busca de variáveis builtin:

```c
// ceval.c
        TARGET(LOAD_GLOBAL_BUILTIN) { // 3085
            assert(cframe.use_tracing == 0);
			// Faz a extração do namespace global do frame
            DEOPT_IF(!PyDict_CheckExact(GLOBALS()), LOAD_GLOBAL);
			// Faz a extração do namespace builtins
            DEOPT_IF(!PyDict_CheckExact(BUILTINS()), LOAD_GLOBAL);
			
			// Faz o load dos dicionarios
            PyDictObject *mdict = (PyDictObject *)GLOBALS();
            PyDictObject *bdict = (PyDictObject *)BUILTINS();
			
			// Inicia o mecanismo de cache
            _PyLoadGlobalCache *cache = (_PyLoadGlobalCache *)next_instr;
            uint32_t mod_version = read_u32(cache->module_keys_version);
            uint16_t bltn_version = cache->builtin_keys_version;
			
			// valida se as versões do cache e o objeto são as mesmas
            DEOPT_IF(mdict->ma_keys->dk_version != mod_version, LOAD_GLOBAL);
            DEOPT_IF(bdict->ma_keys->dk_version != bltn_version, LOAD_GLOBAL);
			// ...
        }
```

Nesse caso, antes da instrução otimizada ser executada, diversas perguntas serão feitas pelo interpretador:

1. A versão do namespace global é a mesma?
2. A versão do namespace builtin é a mesma?

Se forem, a instrução vai usar a adaptação pra prosseguir. Caso não sejam, a operação tradicional (não adaptativa) será executada e o `counter` da struct de cache será decrementado.

Caso o valor do `counter` seja 0 ou menor do que zero, a instrução será convertida na base adaptativa. Voltando para o estado intermediário:

```
LOAD_GLOBAL_BUILTIN -> LOAD_GLOBAL_ADAPTIVE
```

Fazendo o processo inverso ao de quickening. Nesse momento, o bytecode está em um estado transiente, que será modificado na próxima execução de `LOAD_GLOBAL_ADAPTIVE`. Que fará a adaptação para o próximo valor chamado.

### O caso da função de soma

A função de soma tem um comportamento bastante simples para visualizar essa operação. Porém, vamos fazer somente pelo python agora:

Partindo do bytecode já adaptado:

```python
>>> dis(add, adaptive=True, show_caches=True)
  1           0 RESUME_QUICK             0
              2 LOAD_FAST__LOAD_FAST     0 (x)
              4 LOAD_FAST                1 (y)
              6 BINARY_OP_ADD_INT        0 (+)
              8 CACHE                    0 (counter: 53)
             10 RETURN_VALUE
```

Ao performamos a operação contrária a adaptação 53 vezes, temos o bytecode transiente:

```python
>>> [add('', '') for _ in range(53)]
# ...
>>> dis(add, adaptive=True, show_caches=True)
  1           0 RESUME_QUICK             0
              2 LOAD_FAST__LOAD_FAST     0 (x)
              4 LOAD_FAST                1 (y)
              6 BINARY_OP_ADAPTIVE       0 (+)
              8 CACHE                    0 (counter: 501)
             10 RETURN_VALUE
```

O bytecode ficará no estado transiente por `501` (esse valor não significa realmente 501 chamadas). Podemos chamar com unicode novamente:

```python
>>> add('', '')
''
>>> dis(add, adaptive=True, show_caches=True)
  1           0 RESUME_QUICK             0
              2 LOAD_FAST__LOAD_FAST     0 (x)
              4 LOAD_FAST                1 (y)
              6 BINARY_OP_ADAPTIVE       0 (+)
              8 CACHE                    0 (counter: 485)
             10 RETURN_VALUE
```

Agora o valor do contador caiu para `485`. Vamos "esquentar" um pouco esse código:

```python
>>> [add('', '') for _ in range(100)]
# ...

>>> dis(add, adaptive=True, show_caches=True)
  1           0 RESUME_QUICK             0
              2 LOAD_FAST__LOAD_FAST     0 (x)
              4 LOAD_FAST                1 (y)
              6 BINARY_OP_ADD_UNICODE     0 (+)
              8 CACHE                    0 (counter: 53)
             10 RETURN_VALUE
```

Temos o opcode readaptado para `BINARY_OP_ADD_UNICODE` e esse ciclo será feito durante todo o runtime.
