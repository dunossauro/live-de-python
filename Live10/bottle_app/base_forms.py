from wtforms import Form, TextField, PasswordField, SubmitField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.fields import DateField


class Cadastro(Form):
    name = TextField('Nome')
    lastName = TextField('Sobrenome')
    username = TextField('Usuário')
    passwd = PasswordField('Senha')
    email = EmailField('Email')
    gender = SelectField('Sexo', choices=[('masculino', 'Masculino'),
                                          ('feminino', 'Feminino')])
    btnSend = SubmitField('Enviar')
    age = DateField('Nascimento', format='%d/%m/%Y')


class Login(Form):
    username = TextField('Usuário')
    password = PasswordField('Senha')
    btnLogin = SubmitField('Entrar')
