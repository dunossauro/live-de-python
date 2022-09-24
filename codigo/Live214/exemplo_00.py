from rocketry import Rocketry
from rocketry.conds import minutely, every

app = Rocketry()


@app.task(every('2s'))
def a_cada_segundo():
    print('A cada 10 segundos')


@app.task(minutely)
def a_cada_minuto():
    print('Estou sendo executada a cada minuto!')


@app.task('every 1 hour')
def a_cada_hora():
    print('Estou sendo executada a cada hora!')


app.run()
