"""Criando pipelines."""
from random import randint
from rocketry import Rocketry
from rocketry.conds import after_fail, after_success

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
