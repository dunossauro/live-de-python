# Namespaces

Um dos problemas que surgem quando utilizamos decoradores e o paradigma funcional são os namespaces. Eles podem ficar BEM confusos e convolutos. Falei disso por cima lá na nota que a gente junta tudo pra começar a fazer decoradores, mas o buraco vai mais fundo. Por exemplo, vamos pegar novamente o decorador `guarda_parametro`

```python
def guarda_parametros(param):
    # param é minha freevar
    def decorador(func):
        def closure(*args, **kwargs):
            """Docstring Closure"""
            print(param) # funciona!
            print(func.__name__)
            return func(*args, **kwargs)
        return closure
    return decorador

@guarda_parametros('parametro!')
def soma(x, y):
    """Docstring Soma"""
    return x+y

soma(1, 1)
# parametro!
# soma
# 2

soma
# function __main__.guarda_parametros.<locals>.decorador.<locals>.closure(*args, **kwargs)>

soma.__name__ # 'closure'
soma.__doc__ # 'Docstring Closure'
```

Epa, o que ta acontecendo aqui?? O objeto ser diferente já discutimos, mas e esse `__name__` e esse `__doc__`? Acontece que o name `soma` agora aponta pra um objeto novo, com os metadados daquele objeto. Po, aí não! Construi minha função, escolhi um nome maneiro, documentei ela direitinho, pra ela perder tudo por causa de um decorador?

Pois bem, existe uma forma de evitar isso: a função `wraps` da `functools`. Pra fazer isso, vou colocar esse decorador decorando uma função DENTRO da definição de um decorador pra resolver o problema de namespace. AHN?? Sim, vem co pai. Lembra que o decorador é um Wrapper: pega uma função (wrapped), envelopa ela com varias coisas, e devolve o Wrapper. O que a função `wraps` vai fazer é atualizar esse Wrapper pra se parecer com a minha função Wrapped.

Vou usar a forma geral do decorador com parametros

```python
from functools import wraps

def guarda_parametros(param):
    # param é minha freevar
    def decorador(func):
        @wraps(func) # sim, decorei a closure
        def closure(*args, **kwargs):
            print(param)
            print(func.__name__)
            return func(*args, **kwargs)
        return closure
    return decorador

@guarda_parametros('parametro!')
def soma(x, y):
    """Docstring Soma"""
    return x+y

soma(1, 1)
# parametro!
# soma
# 2

soma
# <function __main__.soma(x, y)>

soma.__name__ # 'soma'
soma.__doc__ # 'Docstring Soma'
```

Resolvido!! O `wraps` pega uma closure, e passa essa closure pra uma nova função que vai fazer uma nova closure que vai fazer mais coisa que vai fazer...... e assim vai embora. O importante é que no final, eu resolvi o meu problema: a minha função foi copiada de volta pro namespace da `__main__`, e eu não tenho mais aquele namespace feião, mas ainda mantendo os parametros que eu passei pra esse decorador e as minhas docstrings e nomes. Mágico, né?
