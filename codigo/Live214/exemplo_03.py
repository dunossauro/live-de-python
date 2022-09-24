import logging
from random import randint
from rocketry import Rocketry
from rocketry.conds import (
    after_success, after_finish, after_all_finish
)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
task_logger = logging.getLogger('rocketry.task')
task_logger.addHandler(handler)

app = Rocketry()


@app.task('every 3s')
def todo_segundo():
    if randint(0, 1):
        raise Exception('Quebrou!')
    print('Sucesso!')


@app.task(after_success(todo_segundo))
def todo_segundo_deu_certo():
    print('Depois do Sucesso!')


@app.task(
    after_all_finish(todo_segundo, todo_segundo_deu_certo)
)
def todo_segundo_acabou():
    print('Todo Segundo Acabou!')




app.run()
