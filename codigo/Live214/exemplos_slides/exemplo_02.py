"""Exemplo da sintaxe extendida."""
from rocketry import Rocketry
from rocketry.conds import every

app = Rocketry()


@app.task('every 1s')
def a_cada_segundo():
    ...


@app.task('every 1 day')
def a_cada_dia():
    ...


@app.task(every('1d'))
def a_cada_dia():
    ...


@app.task(every('1s'))
def a_cada_segundo():
    ...


app.run()
