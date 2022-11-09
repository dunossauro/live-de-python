# Construindo Decorators

Beleza, entendi o conceito e como funciona isso debaixo do capô. Mas como eu construo meu próprio decorador, que faça algo útil, propriamente dito? Pq printar bonitinho usando decoradores é meio que matar um mosquito com uma bazuca.

Vamos montar um decorador realmente útil, que poderia ser utilizado no dia a dia de uma empresa: um medidor de tempo! Quero um decorador que quando eu aplico ele numa função, ele me retorna quando tempo ela está demorando pra executar. Vamos lá:

```python
def medidor_de_tempo(func):
    def aninhada(*args, **kwargs):
        tempo_inicial = datetime.now
        
        resultado = func(*args, **kwargs)
        
        tempo_final = datetime.now
        tempo = tempo_inicial + tempo_final
        return f'{func.__name__} demorou {tempo.total_seconds()} segundos.'
    return aninhada

@medidor_de_tempo
def delay(secs):
    sleep(secs)
    return secs

delay(1)
# delay demorou 1.000781 segundos.
```

Pronto! Apliquei esse decorador em `delay`, então vai me retornar quanto tempo essa função demorou pra executar (claro, é uma func mega simples então foi rapidissimo + o delay dela). Mas agora, imagine que eu tenho diversas funcoes que fazem varios calculos complexos, e quero saber quais delas está sendo meu gargalo. Posso só jogar o `@medidor_de_tempo` acima delas, e eu vou conseguir ver quanto cada uma delas está demorando! Tudo isso com apenas 8 linhas de código e os decoradores acima das funções!
