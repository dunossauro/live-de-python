from json import loads

from behave import when, then
from requests import get, post


@when(u'faço uma requisição na url "{url}"')
def request_url(context, url):
    context.response = get(url='{}{}'.format(context.base_url, url))


@then(u'a api deve responder')
def check_response_json(context):
    assert context.response.json() == loads(context.text)


@when(u'faço uma requisição POST na url "{url}"')
def post_request_json(context, url):
    headers = {'Content-Type': 'application/json'}
    context.response = post(url='{}{}'.format(context.base_url, url),
                            json=loads(context.text), headers=headers)
    assert False
    
