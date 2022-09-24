"""Criando pipelines."""
from random import randint
from rocketry import Rocketry
from rocketry.conds import after_success
from rocketry.args import Return

app = Rocketry()


@app.task('every 1 second', name='A')
def tarefa_A():
    if randint(0, 1):
        raise Exception('Error')
    else:
        return 'Sucesso'


@app.task(after_success(tarefa_A))
def tafera_para_sucesso_de_A(value=Return(tarefa_A)):
    print('Retorno de A: ', value)


app.run()
