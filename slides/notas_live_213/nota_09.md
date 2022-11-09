# Juntando o megazord: Decorators

Depois de ver isso tudo, finalmente vamos poder definir formalmente o que é um decorador!!

## Definindo Decorators

Uma Closure pode ser um Decorador se:

- A closure recebe uma função
- A função recebida é uma variável livre
- Retorna a função interna da closure

Sim, é bem específico. Veja um exemplo:

```python
def decorador(func):
    def interna(*args):
        resultado = func(*args)
        return f'Sou uma closure, e sua func retornou: {resultado}'
    return interna

def soma(x, y):
    return x+y

decorada = decorador(soma)
print(decorada(1, 2))
# 'Sou uma closure, e sua func retornou: 3'
```

Repare que não usei `nonlocal` pq não preciso modificar a func, mas poderia usar se necessário.

Aqui, esse código vai criar uma nova função, que vai fazer exatamente a mesma coisa que a função `soma`, mas deixar ela mais decorada, mais bonitinha: ele executa a `soma`, pega esse resultado, e imbute ele numa string bacaninha.

Agora que vem o pulo do gato: o **decorador** nada mais é do que uma forma fácil e rápida de escrever essa closure. Ao invés de eu precisar passar uma função pra closure, armazenar a função resultante em uma nova variável, e aí sim chamar essa função resultante, eu posso só decorar uma função com esse comportamento:

```python
def decorador(func):
    def interna(*args):
        resultado = func(*args)
        return f'Sou uma closure, e sua func retornou: {resultado}'
    return interna

@decorador
def soma(x, y):
    return x+y

soma(1, 2)
# 'Sou uma closure, e sua func retornou: 3'
```

Wow!! Meu código fica muito mais limpo e fácil de ler!
Além disso, fica bem simples reaproveitar esse decorador. Por exemplo:

```python
@decorador
def inverte(texto: str):
    return texto[::-1]

inverte('harry')
# 'Sou uma closure, e sua func retornou: yrrah'
```

Além disso, não preciso mais de uma funcao auxiliar, eu posso simplismente adicionar essa nova funcionalidade na funcao, e estou pronto pra ir!! Peraí, vamos com calma que não é bem assim...

## Debaixo do capô

Vale eu deixar aqui uma observação: Com o decorador, eu não estou 'extendendo a funcionalidade de uma função', 'adicionando novas ferramentas pra essa função', nem nada do tipo. Eu estou transformando a função. Na verdade, sendo mais específico: a minha função `soma`, depois de decorada, *não é mais a mesma função*.

Peraí, que? Sim, é isso mesmo. Pra entender melhor, vamos chamar a **variavel** `soma` antes e depois de ser decorada:

```python
soma # sem decorador
<function __main__.soma(x, y)>

soma # com decorador
<function __main__.decorador.<locals>.interna(*args)>
```

Mas o que diabos está acontecendo aqui? Eu te explico: debaixo dos panos o que o `@decorador` está fazendo é apenas chamar a closure passando a minha função. Se eu tivesse chamado a função auxiliar `decorada` depois de executar a linha `decorada = decorador(soma)`, teria o mesmo resultado. Pq a closure está me retornando a funcao `interna`. A única diferença é que agora, a **variável** `soma` não está mais apontando para a minha **função** `soma`, e sim para a função `interna`, retornada pela closure (lembre-se: `soma` é só um nome que aponta para um objeto, que no caso é uma função). Pra sumarizar:

```python
def soma(x, y):
    return x+y
soma 
# <function __main__.soma(x, y)>

decorador(soma)
# <function __main__.decorador.<locals>.interna(*args)>

soma = decorador(soma)
soma
# <function __main__.decorador.<locals>.interna(*args)>
```

```python
@decorador
def soma(x, y):
    return x+y
soma
# <function __main__.decorador.<locals>.interna(*args)>
```
