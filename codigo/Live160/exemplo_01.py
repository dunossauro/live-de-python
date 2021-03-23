from datetime import datetime
from peewee import (
    SqliteDatabase, Model, TextField, ForeignKeyField,
    DateTimeField, IntegerField
)


db = SqliteDatabase('notas.db')


class BaseModel(Model):
    class Meta:
        database = db


class Pessoa(BaseModel):
    nome = TextField()
    email = TextField(unique=True)
    senha = TextField()
    idade = IntegerField()


class Grupo(BaseModel):
    nome = TextField()
    dona = ForeignKeyField(Pessoa, backref='grupos')


class Nota(BaseModel):
    dona = ForeignKeyField(Pessoa, backref='notas')
    grupo = ForeignKeyField(Grupo, backref='notas', null=True, default=None)
    titulo = TextField()
    nota = TextField()
    criada_em = DateTimeField(default=datetime.now)
    modificada_em = DateTimeField(default=datetime.now)


Pessoa.create_table()
db.create_tables([Grupo, Nota])
