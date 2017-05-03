from behave import step_matcher

@step('acessar a pagina "{page}"')
def acess_page(context, page):
    context.ff.get('http://127.0.0.1:8080/')

@step('deve aparecer na pagina a string "{string}"')
def test_html(context, string):
    assert string in context.ff.page_source, \
        'O texto não foi encontrado na página'
