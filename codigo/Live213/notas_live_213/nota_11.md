# Parametros para Decorators

Agora, vamos um nível além: existem decoradores que recebem parametros!! Eita, como assim? Vamos a um exemplo: o Flask!

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>
```

Eita, mas que que está acontecendo aqui? O decorador não tinha que ser uma função recebendo uma função? Como eu posso fazer ele receber outras variáveis também? Facil: colocando isso dentro de mais uma função! Calma, não chora, vai dar certo, vem comigo.

## Reaplicando os conceitos

Lembra, o decorador nada mais é do que um jeito bonitinho de escrever closures, que são funções. Então, eu vou apenas ir aplicando de novo e de novo os conceitos que a gente passou antes! Meio que um croissant, onde vc tem uma massa de pão, e se vc enrola ela nela mesma muitas vezes vc acaba com um pão muito louco e diferente, mas no fundo a massa é a mesma! Aqui, ainda é tudo função, só estou fazendo uma dentro da outra.

Pra podermos passar um parametro pra um decorador, vamos fazer o seguinte: colocar aquela **closure** (que é o meu decorador em sí) dentro de uma **função de ordem superior (HOF)**, que vai armazenar esses parametros na forma de **variaveis livres**. Assim, meu decorador vai poder acessar esses parametros livremente! Isso vai ficar na forma:

```python
def guarda_parametros(param):
    # param é minha freevar
    def decorador(func):
        def closure(*args, **kwargs):
            print(param) # funciona!
            print(func.__name__)
            return func(*args, **kwargs)
        return closure
    return decorador
```

Vamos a um exemplo prático: um decorador pra tentar executar uma função, e caso de um erro que eu esperava, retenta executar a função, até N vezes. Muito útil pra operações instáveis (acessar um banco de dados numa rede ruim, por exemplo). Vamos lá:

```python
# param do decorador: erro esperado e quantas vezes tentar executar
def retry(erro, vezes):
    count = 0
    def intermediaria(func):
        def closure(*args, **kwargs):
            nonlocal count # necessario pois vou alterar
            try:
                return func(*args, **kwargs)
                print(f'{func.__name__} success on try: {count}')
            except error as e:
                count += 1
                print(f'{func.__name__} error: {e} retry: {count}')
                if count < vezes:
                    return closure(*args, **kwargs)
        return closure
    return intermediaria
```

Agora, vamos chamar esse decorador numa função que eu espero que de um erro de valor (dividir por 0, por ex.). Claro que sempre vai dar erro, mas é só pra termos uma ideia.

```python
# caso tenha esse erro, tenta de novo ate 5 vezes
@retry(ZeroDivisionError, 5)
def div(x, y):
    return x/y

div(3, 0)
# div error: division by zero retry: 1
# div error: division by zero retry: 2
# div error: division by zero retry: 3
# div error: division by zero retry: 4
# div error: division by zero retry: 5
```

De novo, isso vai sempre dar erro pq sempre estou tentando dividir por zero sempre, mas é bom pra pegar a ideia. Viu como esse conceito é extremamente poderoso?
