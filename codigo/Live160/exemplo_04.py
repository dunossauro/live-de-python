from hashlib import sha512
from exemplo_01 import db, Pessoa
from peewee import fn


@db.func()
def encripta_senha(senha):
    return sha512(senha.encode('utf-8')).hexdigest()


@db.func()
def batata(senha):
    return sha512(senha.encode('utf-8')).hexdigest()


Pessoa.create(
    nome='Criptografada',
    senha=fn.encripta_senha('1234'),
    email='cipt2@grafia.com',
    idade=25
)


Pessoa.select().where(fn.batata())
