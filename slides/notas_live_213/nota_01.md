# O que são Decorators? Uma compreensão prática

Decoradores são os `@` acima de alguma função, classe, método, etc. da forma:

```python
@decorator
def func(x):
    return(x)
```

Na prática, é uma função aplicada nas minhas funções. Um exemplo é:

```python
@cache
def delay(seconds):
    sleep(seconds)
    return(seconds)
```

Essa função apenas bota o códio pra dormir. Aqui, o decorador `@chache` (que pode ser aplicado em qualquer função) armazena o resultado, e só vai me retornar direto pra valores que já foram rodados. Então chamar `delay(10)` vai dormir o código por 10 sec. Se eu chamar o `delay(10)` de novo, o decorador `cache` vai entender que esse código já foi rodado e que eu já sei o resultado, então ele só me da o `return(seconds)` (nesse caso, 10), e não vai botar o código pra dormir 10 segundos.

Mas qual a definição formal?

## Definição formal

Decoradores são açúcar sintático para closures.

Ok, não ajudou muito kkkkkkk. Isso é pq Decorators são um assunto um pouco complexo, apesar de serem simples: eles envolvem diversar partes e detalhes do python, que de cara não são óbvias. Então, agora eu vou tentar documentar todas essas partes diferentes do python, e como elas funcionam interagem entres sí para chegarmos no decorador, e ultimamente para que essa definição formal seja fácil e intuitiva de se entender.
