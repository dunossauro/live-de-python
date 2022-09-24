"""Rocketry executando `a_cada_minuto` todos os minutos."""
from rocketry import Rocketry
from rocketry.conds import minutely

app = Rocketry()


@app.task(minutely)
def a_cada_minuto():
    print('Executando tarefa a cada minuto')


app.run()
