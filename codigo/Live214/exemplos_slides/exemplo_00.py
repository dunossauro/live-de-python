"""Rocketry executando `a_cada_minuto` todos os minutos."""
from rocketry import Rocketry

app = Rocketry()


@app.task('minutely')
def a_cada_minuto():
    print('Executando tarefa a cada minuto')


app.run()
