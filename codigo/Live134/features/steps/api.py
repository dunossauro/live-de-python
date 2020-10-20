from ast import literal_eval

from behave import given, when, then
from httpx import get, post


@given('que exista uma tarefa')
def inserir_tarefa(context):
    feature_table = context.table['0']
    tarefa = {}
    tarefa['title'] = feature_table['nome']
    tarefa['description'] = feature_table['descrição']
    tarefa['done'] = feature_table['estado']

    assert post(context.base_url, json=tarefa).status_code == 201


@when('verificar minhas tarefas em "{endpoint}"')
def get_minhas_tarefas(context, endpoint):
    context.request = get(context.base_url)


@then('não devo ter nenhuma tarefa para fazer')
def checando_se_não_tenho_nenhuma_tarefa(context):
    assert context.request.json() == []


@then('devo ter a seguinte tarefa para fazer')
def checar_se_tarefa_esta_para_ser_feita(context):
    feature_table = context.table['0']
    tarefa = {}
    tarefa['title'] = feature_table['nome']
    tarefa['description'] = feature_table['descrição']
    tarefa['done'] = literal_eval(feature_table['estado'])
    response = context.request.json()
    del response[0]['id']


    assert tarefa in response, f'{response} {tarefa}'
