# Ao infinito e além

Bom, chegamos ao final dessa jornada. Mas isso é só um pedaço do que podemos fazer com decoradores. Isso pq na realidade, esse é o pedaço fundamental: a base de tudo. A partir do que foi aprendido aqui, vc já tem a base para expandir, construir, iterar e aumentar decoradores e funções. Os decoradores nada mais são do que uma forma bonitinha de fazer uma programação no **paradigma funcional**. Tudo que eu posso aplicar em funções posso aplicar pra decoradores.

Na última nota, eu decorei uma Closure na definição de um outro decorador. Você reparou que na nota sobre parametros para decoradores, no decorador que construímos a Closure era recursiva? Pois é! Se eu quisesse, poderia colocar dois decoradores (um decora o outro que decora a função).

Ou ainda: podemos decorar métodos!

```python
def decorador_metodo(func):
    def interna(self, *args **kwargs):
        return func(self, *args **kwargs)
    return interna

class Classe:
    @decorador_metodo
    def metodo():
        return True
```

Ou Classes!!

```python
def decora_classe(classe):
    def inner(*args **kwargs):
        return classe(*args **kwargs)
    return inner

@decora_classe
class Classe
    ...
```

Esses decoradores não estão fazendo nada, claro, mas serve pra ilustrar o meu ponto: o que eu passei aqui é o contexto sobre decoradores, agora vc pode aplicar onde e como você quiser!

Vá ao infinito e além!
**Godspeed!**
