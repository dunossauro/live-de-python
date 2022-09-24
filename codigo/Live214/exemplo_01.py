from rocketry import Rocketry
from rocketry.conds import minutely

app = Rocketry()


@app.task(minutely.between('10', '50'))
def restrições():
    print('Minuto depois do 10')


# @app.task('hourly after 10')
# def restrições():
#     print('Minuto depois do 10')


app.run()
