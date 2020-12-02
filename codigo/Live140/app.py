from flask import Flask, render_template, request
from wtforms import Form, validators
from wtforms.fields import (
    StringField,
    PasswordField,
    SubmitField,
    RadioField,
    SelectField
)
from wtforms.fields.html5 import EmailField
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
import gettext

gettext.install('', '')

app = Flask('meuapp')
app.config['SECRET_KEY'] = 'batatinahsfritasvoadoas321123'
csrf = CSRFProtect(app)


class FormCadastro(FlaskForm):
    nome = StringField('Nome')
    email = EmailField('Seu Email')
    pergunta = RadioField(
        'Você gosta mais de',
        choices=['Batata', 'Estudar']
    )
    escolha = SelectField(
        'Escolha', choices=['Cerveja', 'Café']
    )
    senha = PasswordField(
        'Sua senha',
        [
            validators.EqualTo(
                'senha_confirm',
                message=_('As senhas são diferentes')
            ),
            validators.Length(
                min=6, max=20,
                message=_('O tamanho precisa ser entre %(min)d e %(max)d')
            )
        ]
    )
    senha_confirm = PasswordField('Confirme sua senha')
    btn = SubmitField('Criar')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = FormCadastro(request.form)
    if request.method == 'POST' and form.validate():
        return 'OK'

    return render_template(
        'cadastro.html',
        form=form
    )


app.run()
