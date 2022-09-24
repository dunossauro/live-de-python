from rocketry import Rocketry
from rocketry.args import FuncArg, Arg

from func import data_atual

app = Rocketry()
app.params(
    batatinha='fritas'
)


@app.task('every 3s')
def todo_3_segundos(hoje=Arg('batatinha')):
    print(hoje)


# app.run()
