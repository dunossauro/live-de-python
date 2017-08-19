from bottle import Bottle, jinja2_view
from wtforms import StringField, Form, SubmitField
from wtforms.fields.html5 import EmailField

app = Bottle()


class Cadastro(Form):
    name = StringField('Username')
    phone = StringField('Phone')
    email = EmailField('Email')
    butt = SubmitField('OK!')


@app.route('/cadastro', methods=['GET', 'POST'])
@jinja2_view('./index.html')
def index():
    return dict(title='Cadastro',
                form=Cadastro())


app.run()
