# Interpretador adaptativo especializado

> TODO: Explicar em poucas palavras que porra é essa

## Funções de estudo

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

## Compilação

Quando um objeto de código (code) é criado pelo quadro (frame). Um dos atributos do código é `co_warmup`.

`co_warmup` é populado com a constante `QUICKENING_INITIAL_WARMUP_VALUE`. Que tem o valor de `-8`.

Durante o processo de compilação é inserido como primeira instrução do bytecode um operação chamada [`RESUME`](https://docs.python.org/pt-br/3.11/library/dis.html#opcode-RESUME).


## Aquecimento no runtime
Durante a execução do bytecode, todas as vezes em que a operação `RESUME` for executada, o valor atribuído a `co_warmup` é decrementado em `-1`.


## Processo de aceleração (Quickening)

Quando o valor presente em `co_warmup` chegar a `0`. O processo de aceleração será inicializado.

### Aceleração 

O processo de aceleração é uma etapa de substituição de algumas instruções (opcodes) no bytecode por suas versões mais rápidas ou adaptáveis.

#### Super instruções

Uma das formas de transformar a execução do bytecode em mais "rápida" é reduzir o número de operações durante a interpretação. Uma dessas formas é "compilar" um grupo de instruções em uma única instrução.

Damos o nome de super instrução (superinstruction) para essas instrução.

Na versão 3.11, todas as operações de `LOAD_FAST` e `STORE_FAST` quando encontradas em sequência serão otimizadas para uma super instrução. Por exemplo em nossa função de soma:

```python
>>> dis(add)
  1           0 RESUME                   0
              2 LOAD_FAST                0 (x)
              4 LOAD_FAST                1 (y)
              6 BINARY_OP                0 (+)
             10 RETURN_VALUE
```

Existe uma sequência de LOAD_FAST, pois duas variáveis são carregas em sequência. No momento da aceleração elas serão convertidas em uma única super instrução chamada `LOAD_FAST__LOAD_FAST`:

```python
# ...
              2 LOAD_FAST__LOAD_FAST         0 (x)
              4 LOAD_FAST                    1 (y)
			  6 BINARY_OP_ADAPTIVE           0 (+)
             10 RETURN_VALUE
```

> obs: Embora o segundo `LOAD_FAST` ainda exista no bytecode, a instrução anterior vai "pular" esse opcode durante a execução do loop do interpretador.

#### Instruções adaptáveis

No momento da aceleração algumas instruções serão substituídas pelas suas variantes adaptáveis. Uma operação adaptável é uma operação de estado intermediário de otimização.

Por exemplo, a soma no python acontece com o opcode `BINARY_ADD`. Uma operação genérica que resolve qualquer tipo de operação entre dois termos. Como `1+1`, `1-1`, `1>>0`, ...

Durante a aceleração, essa operação será trocada por `BINARY_OP_ADAPTIVE`. A variante que permite adaptação.

Outro exemplo é a operação `LOAD_GLOBAL` que busca por nomes nos namespaces global e builtin. Será troacada pela sua versão adaptável `LOAD_GLOBAL_ADAPTIVE`.

#### Cache embutido

Durante as trocas por instruções adaptáveis, o bytecode adiciona uma nova instrução chamada `CACHE`. A instrução de `CACHE` sempre é seguinte a uma operação adaptável ou especializada.

O número de caches também pode variar em relação a instrução. Por exemplo:

```python
OP_ADAPTIVE
CACHE  (counter: 0)
CACHE  (variável: 'abc')
```

As operações de `CACHE` nunca serão executadas pelo interpretador. Elas são complementares a instrução que "embute" o cache.


##### O contador

Embora existam vários valores sendo armazenados em cache. Um dele tem uma especial para as transformações do bytecode que é o `counter`. Todas as operações de adaptáveis e especializadas contam com ele.


#### Como isso acontece?

> TODO: explicar as coisas com código do cpython


## Especialização

O processo de especialização é a consequência das instruções adaptáveis em conjunto com o cache. Quando essas instruções adaptáveis são executadas pelo interpretador (ceval.c), o valor do contador do cache será avaliado.

Caso o counter da operação adaptável esteja em `0`, ela sera substituída por uma operação especializada.

Por exemplo, vamos supor que estejamos trabalhando com uma operação de soma `1 + 1`:

```
Aquecimento -> Aceleração         -> Especialização
BINARY_OP   -> BINARY_OP_ADAPTIVE -> BINARY_OP_ADD_INT
```

### Cache

> TODO: explicar o mecanismo do cache e seus decrementos

### "des-especialização"
