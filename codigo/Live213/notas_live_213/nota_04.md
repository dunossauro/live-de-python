# Funções de ordem superior (HOF)

Uma função de ordem superior é uma função que recebe ou retorna outra função.

## Funcs recebendo funcs

Veja o exemplo da função `filter` que filtra meus elementos. A questão é que ela é uma função de ordem superior, pois pode ordenar utilizando uma função que eu passar como parâmetro pra ela:

```python
def maior_que_cinco(x):
    return x>5

resultado = filter(maior_que_cinco, [3,4,5,6,7])
print(list(resultado)) # 6, 7
```

## Funcs retornando funcs

Existe uma função chamada `partial` que serve pra fixar um dos parametros de uma outra função. Ela vai receber uma função (como o `filter` acima), e um parametro, e vai retornar uma função com esse parametro congelado:

```python
from functools import partial
def soma(x, y):
    return x+y

# Agora o parametro x é sempre 10
soma_10 = partial(soma, x=10)
soma_10(1) # retorna 11
```

Isso pode ser um pouco confuso no início, já que `partial` devolve uma função e depois preciso chamar ela novamente. Mas é questão de costume, essa é uma lógica bem comum no paradigma funcional. Mas para entender como construir uma função que retorna outras, primeiro precisamos entender as **funções aninhadas**.
