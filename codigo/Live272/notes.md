DIAGRAMA: https://excalidraw.com/#json=QouxLypjA239k4s1YKpNd,5rkGdZESVyFG94_U2JQhJQ

# [Resumo] Como o bytecode é gerado

Processo de compilação:

Tokenize -> Parser -> AST -> Bytecode

## Token

```python
○ → python -m tokenize exemplo.py 
0,0-0,0:            ENCODING       'utf-8'
1,0-1,3:            NAME           'def'
1,4-1,7:            NAME           'add'
1,7-1,8:            OP             '('
1,8-1,9:            NAME           'x'
1,9-1,10:           OP             ','
1,11-1,12:          NAME           'y'
1,12-1,13:          OP             ')'
1,13-1,14:          OP             ':'
1,15-1,21:          NAME           'return'
1,22-1,23:          NAME           'x'
1,24-1,25:          OP             '+'
1,26-1,27:          NAME           'y'
1,27-1,28:          NEWLINE        '\n'
2,0-2,0:            ENDMARKER      ''
```

## ast

```python
○ → python -m ast exemplo.py 
Module(
   body=[
      FunctionDef(
         name='add',
         args=arguments(
            args=[
               arg(arg='x'),
               arg(arg='y')]),
         body=[
            Return(
               value=BinOp(
                  left=Name(id='x', ctx=Load()),
                  op=Add(),
                  right=Name(id='y', ctx=Load())))])])
```

## bytecode

```python
○ → python -m dis exemplo.py 
  0           RESUME                   0

  1           LOAD_CONST               0 (<code object add at 0x7b7031d8a5d0, file "exemplo.py", line 1>)
              MAKE_FUNCTION
              STORE_NAME               0 (add)
              RETURN_CONST             1 (None)

Disassembly of <code object add at 0x7b7031d8a5d0, file "exemplo.py", line 1>:
  1           RESUME                   0
              LOAD_FAST_LOAD_FAST      1 (x, y)
              BINARY_OP                0 (+)
              RETURN_VALUE
```


# Como o interpretador interpreta

> TODO: HEAP / Stack / Frame / Namespace

## Stack Machine

## Stack Frame

## [Instruções](https://docs.python.org/pt-br/3/library/dis.html#python-bytecode-instructions)

Python 3.11: https://github.com/python/cpython/blob/3.11/Python/ceval.c#L1759
Python 3.12:
- switch: https://github.com/python/cpython/blob/3.12/Python/ceval.c#L843
- opcodes: https://github.com/python/cpython/blob/3.12/Python/generated_cases.c.h


# PEP 659 – Specializing Adaptive Interpreter

https://docs.python.org/3/whatsnew/3.11.html#pep-659-specializing-adaptive-interpreter


## Bytecode

Vamos iniciar observando uma operação bastante simples, uma função de soma:

```py
def add(x, y): return x + y
```

As instruções de bytecode associadas a qualquer bloco de código podem ser vistas usando a função `dis.dis`.

### Python 3.10

Um exemplo do resultado na versão 3.10.14:

```python
>>> from dis import dis
>>> dis(add)
  1           0 LOAD_FAST                0 (x)
              2 LOAD_FAST                1 (y)
              4 BINARY_ADD
              6 RETURN_VALUE
```

#### As operações do bytecode

- LOAD_FAST: Coloca a referência na stack
- BINARY_ADD (disponível até a 3.10): Soma o TOP e o POP
- RETURN_VALUE: Retorna o valor do TOP

### Python 3.11

O mesmo exemplo na versão 3.11.9:

```python
>>> dis(add)
  1           0 RESUME                   0
              2 LOAD_FAST                0 (x)
              4 LOAD_FAST                1 (y)
              6 BINARY_OP                0 (+)
             10 RETURN_VALUE
```

#### Operação `RESUME`

A operação de `RESUME` não é uma operação propriamente dita. Ela é caracterizada como uma "não operação". É a função do interpretador de ir para um frame específico na stack.

Ela é responsável por tracing interno, debugging e **checagem de otimizações**. Ela pode ter 4 valores, onde:

- 0: O início de uma função
- 1: Após um `yield`
- 2: Após um `yield from`
- 3: Após um `await`

> TODO: Olhar o código fonte da operação de [RESUME](https://github.com/python/cpython/blob/3.11/Python/ceval.c#L1770)

##### Otimização

A instrução de `RESUME` vai checar a contagem de `warmup` do frame e adicionar mais 1:

**ceval**

```c
        TARGET(RESUME) {
            _PyCode_Warmup(frame->f_code);
            JUMP_TO_INSTRUCTION(RESUME_QUICK);
        }
```
https://github.com/python/cpython/blob/795f2597a4be988e2bb19b69ff9958e981cb894e/Python/ceval.c#L1770-L1773

**Warmup**

O valor inicial do frame é definido em [QUICKENING_WARMUP_DELAY](https://github.com/python/cpython/blob/795f2597a4be988e2bb19b69ff9958e981cb894e/Include/internal/pycore_code.h#L95-L96). Na versão 3.11 é de -8.

```c
static inline void
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

https://github.com/python/cpython/blob/795f2597a4be988e2bb19b69ff9958e981cb894e/Include/internal/pycore_code.h#L102-L111

**quicken**

Por exemplo, se a instrução `LOAD_FAST` tiver uma chamada anterior de

- `LOAD_FAST`
- `STORE_FAST`
- `LOAD_CONST`

O interpretador criará uma operação única para representar as duas operações

```c
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

https://github.com/python/cpython/blob/795f2597a4be988e2bb19b69ff9958e981cb894e/Python/specialize.c#L259-L260

Transformando a sequência

```python
>>> dis(add)
  1           0 RESUME                   0
              2 LOAD_FAST                0 (x) # AQUI
              4 LOAD_FAST                1 (y) # AQUI
              6 BINARY_OP                0 (+)
             10 RETURN_VALUE
```

Em:

```python
>>> dis(add, adaptive=True)
  1           0 RESUME_QUICK             0
              2 LOAD_FAST__LOAD_FAST     0 (x)  # AQUI
              4 LOAD_FAST                1 (y)
              6 BINARY_OP_ADD_INT        0 (+)
             10 RETURN_VALUE
```


#### Adaptive

Na versão 3.11 do python a função `dis.dis` ganhou o parâmetro `adaptive`, que permite ver as alterações que o bytecode faz em tempo de execução:

```python
>>> dis(add, adaptive=True)
  1           0 RESUME                   0
              2 LOAD_FAST                0 (x)
              4 LOAD_FAST                1 (y)
              6 BINARY_OP                0 (+)
             10 RETURN_VALUE
```

Em suma, essa operação não muda o resultado das instruções.

Quando a função de soma é executada algumas vezes, o código se torna "quente" [hot code] {diversas chamadas de warmup}. O que faz com que o interpretador se adapte ao que está sendo chamado. Recompilando o bytecode:

```python
>>> [add(1, 1) for _ in range(10)]
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

>>> dis(add, adaptive=True)
  1           0 RESUME_QUICK             0
              2 LOAD_FAST__LOAD_FAST     0 (x)
              4 LOAD_FAST                1 (y)
              6 BINARY_OP_ADD_INT        0 (+)
             10 RETURN_VALUE
```

#### A operação `RESUME_QUICK`

`RESUME_QUICK` diz que o frame já foi adaptado e não precisa mais do processo:

```c
        TARGET(RESUME) {
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

Importante notar que a instrução de `RESUME` tem a função de adicionar o valor de warm, e logo em sequência chama o `RESUME_QUICK` que é a inicialização do frame de fato.

#### Superinstructions

> Explicar operações `RESUME_QUICK`, `LOAD_FAST__LOAD_FAST` e `BINARY_OP_ADD_INT`

---

### Python 3.12

```python
>>> dis(add)
  1           0 RESUME                   0
              2 LOAD_FAST                0 (x)
              4 LOAD_FAST                1 (y)
              6 BINARY_OP                0 (+)
             10 RETURN_VALUE
```

#### quickening

> TODO: Explicar o quickening

```python
>>> dis(add, adaptive=True)
  1           0 RESUME                   0
              2 LOAD_FAST__LOAD_FAST     0 (x)
              4 LOAD_FAST                1 (y)
              6 BINARY_OP                0 (+)
             10 RETURN_VALUE
```

> TODO: LOAD_FAST__LOAD_FAST

### Python 3.13

```python
>>> dis(add)
  1           RESUME                   0
              LOAD_FAST_LOAD_FAST      1 (x, y)
              BINARY_OP                0 (+)
              RETURN_VALUE
```

> quickening: LOAD_FAST_LOAD_FAST


## Quickening

## Adaptive instructions

## Specialization


## Referências

### PEPs

- [PEP 659 – Specializing Adaptive Interpreter](https://peps.python.org/pep-0659/)
- [PEP 744 – JIT Compilation](https://peps.python.org/pep-0744/)

### Documentação

- [Documentação do módulo dis](https://docs.python.org/pt-br/3/library/dis.html)
- [Documentação da função dis.dis](https://docs.python.org/pt-br/3/library/dis.html#dis.dis)
- [Instruções de bytecode](https://docs.python.org/pt-br/3/library/dis.html#python-bytecode-instructions)


## opcodes adaptativos

3.11
```c
const uint8_t _PyOpcode_Caches[256] = {
    [BINARY_SUBSCR] = 4,
    [STORE_SUBSCR] = 1,
    [UNPACK_SEQUENCE] = 1,
    [STORE_ATTR] = 4,
    [LOAD_ATTR] = 4,
    [COMPARE_OP] = 2,
    [LOAD_GLOBAL] = 5,
    [BINARY_OP] = 1,
    [LOAD_METHOD] = 10,
    [PRECALL] = 1,
    [CALL] = 4,
};
```

3.12
```c
const uint8_t _PyOpcode_Caches[256] = {
    [BINARY_SUBSCR] = 1,
    [STORE_SUBSCR] = 1,
    [UNPACK_SEQUENCE] = 1,
    [FOR_ITER] = 1,
    [STORE_ATTR] = 4,
    [LOAD_ATTR] = 9,
    [COMPARE_OP] = 1,
    [LOAD_GLOBAL] = 4,
    [BINARY_OP] = 1,
    [SEND] = 1,
    [LOAD_SUPER_ATTR] = 1,
    [CALL] = 3,
};
```

3.13

```c
const uint8_t _PyOpcode_Caches[256] = {
    [JUMP_BACKWARD] = 1,
    [TO_BOOL] = 3,
    [BINARY_SUBSCR] = 1,
    [STORE_SUBSCR] = 1,
    [SEND] = 1,
    [UNPACK_SEQUENCE] = 1,
    [STORE_ATTR] = 4,
    [LOAD_GLOBAL] = 4,
    [LOAD_SUPER_ATTR] = 1,
    [LOAD_ATTR] = 9,
    [COMPARE_OP] = 1,
    [CONTAINS_OP] = 1,
    [POP_JUMP_IF_TRUE] = 1,
    [POP_JUMP_IF_FALSE] = 1,
    [POP_JUMP_IF_NONE] = 1,
    [POP_JUMP_IF_NOT_NONE] = 1,
    [FOR_ITER] = 1,
    [CALL] = 3,
    [BINARY_OP] = 1,
};
```
