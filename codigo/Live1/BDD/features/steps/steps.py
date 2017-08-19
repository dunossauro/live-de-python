from behave import step
from calc import soma


@step('somar "{val_0}" com "{val_1}"')
def test_soma(context, val_0, val_1):
    context.result = float(soma(float(val_0), float(val_1)))


@step('o resultado deve ser "{resultado}"')
def test_soma_result(context, resultado):
    assert context.result == float(resultado)
