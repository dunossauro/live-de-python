"""Exemplo da sintaxe de restrições."""
from rocketry import Rocketry
from rocketry.conds import weekly, monthly

app = Rocketry()


@app.task('weekly on Monday')
def toda_segunda():
    print('Hoje é segunda')


@app.task('monthly starting 8rd')
def mensal_depois_do_dia_8():
    print('Depois do dia 8')


@app.task(weekly.on('Monday'))
def toda_segunda():
    print('Hoje é segunda')


@app.task(monthly.starting('8rd'))
def mensal_depois_do_dia_8():
    print('Depois do dia 8')


app.run()
