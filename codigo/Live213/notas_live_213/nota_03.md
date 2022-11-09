# Funções como objetos

Em python, funções são objetos. Isso quer dizer que eu posso colocar uma função dentro de uma variável:

```python
def soma(x, y):
    return x+y
sominha = soma
sominha(1, 1) # retorna 2!
```

Também posso colocar dentro de uma lista, tupla, dicionario, etc.:

```python
lista_funcs = [soma, func2, func3]
lista_funcs[0](1, 1) # retorna 2!
```

Isso torna possível criar uma função calculadora, por ex.:

```python
def soma(x, y):
    return x+y
def sub(x, y):
    return x-y
def mult(x, y):
    return x*y
def div(x, y):
    return x/y
def calculadora(operacao, x, y):
    operacoes = {
        '+': soma, '-': sub,
        '*': mult, '/': div
    }
    return operacoes[operacao](x, y)

calculadora('+', 1, 1) # retorna 2!
```

Essas funções estão sendo manipuladas como objetos também são chamadas de **funções de primeira classe**. No python, como todas as funções são objetos, todas as funções são de primeira classe. Mas a distinção existe pois isso nem sempre é verdade em outras linguagens.

Agora vem a parte louca: se eu posso fazer com funções o mesmo que eu posso fazer com objetos, então eu posso passar uma função como parametro de *outra* função!! Essa *outra* função é chamada de **função de ordem superior**
