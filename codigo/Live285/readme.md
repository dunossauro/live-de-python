# Property-based Testing

## Um passo pra trás

Antes de entender o que é de fato property-based, sera interessante lembrar a anatomia de um teste "normal". Por normal, dizemos que o teste é "Example-based testing".

Geralmente, quando temos um bloco de testes, temos algo como AAA. Onde:

- **A**rrange: A organização dos dados que queremos usar no SUT
- **A**ct: A chamada direta ao SUT
- **A**ssert: A verificação se a ação esperada aconteceu

Por exemplo, em uma função simples de soma:

```python
def add(x: int, y: int) -> int:
    return x + y
```

Teríamos um teste como:

```python
def test_add():
   # Arrange: Organização dos dados para o teste
   x, y = 1, 1
   esperado = 2
   
   # Chamada do SUT
   resultado = add(x, y)
   
   # Assert
   assert  resultado == esperado
```

Chamamos esse caso de "example-based" pois pensamos em um "exemplo" de como executar nosso código. Trazendo pra linguagem de especificação, teríamos algo como:

```gherkin
Dado os números 1, 1
Quando chamarmos a função add
Então o resultado deve ser 2
```

Existe uma escolha fixa de exemplares para resolver esse teste. Escolhemos `1` para `x` e `1` para `y`, sabendo que a resposta esperada para esse caso é `2`.


Se olharmos pra isso de uma forma mais "formal", teríamos algo como isso:

<imagem aqui de um gráfico de flechas>


### Parametrização

Sabemos que a função de `add` trabalha com qualquer valor `**qualquer**` valor inteiro. É o esperado... Porém, ao exemplificar, não conseguimos ir muito longe, seriam muitos testes.

Quando as coisas chegam nesse ponto, temos um recurso nativo do pytest como o `parametrize` ou então o `subTest` do Unittest. Onde montamos uma variedade de exemplos e os chamamos todos em um único teste:


```python
@mark.parametrize(
    'x,y,esperado', [(1, 1, 2), (2, 2, 4), (5, 5, 10)]
)
def test_add(x, y, esperado):
   # Chamada do SUT
   resultado = add(x, y)
   
   # Assert
   assert  resultado == esperado
```

Dessa forma, temos uma cobertura um pouco mais interessante:

<imagem aqui de um gráfico de flechas>


Porém, cobrir o oceano de exemplares de inteiro seria impossível, claro, eles são infinitos.


### O problema das bordas

Ainda assim, com mais casos você conseguiria dizer que sua cobertura de exemplares são o suficiente? Quais casos você deixou de cobrir? Se isso fosse um input de usuário, você sabe... Pessoas são bem criativas.

Para cobrir os casos que não sabemos ou podem produzir efeitos imaginários, precisamos de mais dados...


## Property-based

A ideia das propriedades é pensar o "contrário" dos exemplos. É descrever uma propriedade invariante do SUT, definir uma estratégia e deixar o teste fazer mais "com menos". Gosto do slogan do Hypothesis:

> Teste mais rápido, corrija mais

Vamos entender com um exemplo. A soma tem diversas propriedades (não precisamos de todas), como:

- Comutativa
- Elemento neutro

Ou seja, podemos testar essas propriedades sem saber quem são os exemplares. Vamos de exemplo, pra simplificar:

```python
def test_add_comutativo():
    # exemplares
    x, y = 3, 2
	
	# Chamada do sut
	assert add(x, y) == add(y, x)
```

Concorda comigo que independente de quais sejam os exemplares essa operação em teoria tem que dar certo?

Nesse momento o Hypothesis brilha, pois ele oferece estratégias para que isso seja feito de forma simples:

```python
from hypothesis import given
from hypothesis.strategies import integer


@given(integer(), integer())
def test_add_comutativo(x, y):
	assert add(x, y) == add(y, x)
```

Dessa forma, diversas chamadas serão feitas e caso alguma combinação de exemplares não cumpra esse o teste falhará.

Vamos executar:

```shell
pytest .
```

O resultado parece exatamente igual a qualquer teste. Mas o que mudou?

Vamos olhar, sem nos aprofundar no conceito:

```python
@given(integer(), integer())
def test_add_comutativo(x, y):
    print(x, y)
	assert add(x, y) == add(y, x)
```

```shell
pytest -s
```

QUE? QUE ISSO? Meu amigo, quanto dado...

Bom, vamos conversar sobre isso...

### Fuzzing

Fuzzing é uma técnica de randomização em testes para aumentar a cobertura (de exemplares) e encontrar entradas inválidas e/ou inesperadas pelo sistema.

