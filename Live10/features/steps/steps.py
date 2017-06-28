from behave import when, given, then
from selenium import webdriver

dic = {'nome': 'name',
       'sobrenome': 'lastName',
       'usuario': 'username',
       'senha': 'passwd',
       'sexo': 'gender',
       'email': 'email',
       'nascimento': 'age',
       'Enviar': 'btnSend'}


@given('que o usuario esteja na pagina "{page}"')
def open_page(context, page):
    context.ff = webdriver.Firefox()
    context.ff.get(page)


@when('inserir o "{field}" "{value}"')
def insert_values_on_fields(context, field, value):
    context.ff.find_element_by_id(dic[field]).send_keys(value)


@then('clicar no botão "{btn}"')
def click_bnt(context, btn):
    context.ff.find_element_by_id(dic[btn]).click()


@then('a mensagem deverá ser exibida')
def read_text(context):
    page_h1_text = context.ff.find_element_by_id('text').text
    assert context.text == page_h1_text, '''
    {} != {}'''.format(page_h1_text, context.text)
