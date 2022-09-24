from random import randint
from rocketry import Rocketry
from rocketry.conds import after_success
from rocketry.args import Return

app = Rocketry()


@app.task('every 3s')
def todo_3_segundos():
    return randint(1, 10)

@app.task('every 1s')
def todo_segundo():
    return randint(1, 10)


@app.task(
    after_success(todo_segundo)
)
def todo_segundo_deu_certo(
        tres=Return(todo_3_segundos),
        todo=Return(todo_segundo)
):
    print(f'{tres=},{todo=}')




app.run()
