"""Criando pipelines."""
import logging
from random import randint
from rocketry import Rocketry
from rocketry.conds import after_fail, after_success

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
task_logger = logging.getLogger('rocketry.task')
task_logger.addHandler(handler)

app = Rocketry()


@app.task('every 1 second', name='A')
def tarefa_A():
    if randint(0, 1):
        raise Exception('Error')
    else:
        print('A passou')


@app.task(after_fail('A'))
def tafera_para_falha_de_A():
    print('A falhou')


@app.task(after_success(tarefa_A))
def tafera_para_sucesso_de_A():
    print('Sucesso de A')


@app.task("after task 'A' finished")
def tafera_para_fim_de_A():
    print('A terminou')


app.run()
