"""Exemplo da sintaxe de restrições."""
from rocketry import Rocketry
from rocketry.conds import hourly, daily, weekly

app = Rocketry()


# @app.task('hourly before 25:00')
# def toda_hora_antes_do_minuto_25():
#     print('ihu0')


# @app.task('hourly after 01:00')
# def toda_hora_depois_do_minuto_1():
#     print('ihu0 depois')


# @app.task('daily after 23')
# def diariamente_apos_as_23():
#     print('ihu')


# @app.task('daily between 23:00 and 23:59')
# def diariamente_entre_23_e_00():
#     print('ihu2')


# @app.task('weekly between Sunday and Monday')
# def semanalmente_entre_domingo_e_segunda():
#     print('ihu3')


@app.task(hourly.before('25:00'))
def toda_hora_antes_do_minuto_25():
    print('ihu0')


@app.task(hourly.after('01:00'))
def toda_hora_depois_do_minuto_1():
    print('ihu0 depois')


@app.task(daily.after('23:00'))
def diariamente_apos_as_23():
    print('ihu')


@app.task(daily.between('23:00', '23:59'))
def diariamente_entre_23_e_00():
    print('ihu2')


@app.task(weekly.between('Monday', 'Sunday'))
def semanalmente_entre_domingo_e_segunda():
    print('ihu3')

app.run()
