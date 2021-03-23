from peewee import *

database = SqliteDatabase('notas.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Pessoa(BaseModel):
    email = TextField(unique=True)
    idade = IntegerField()
    nome = TextField()
    senha = TextField()

    class Meta:
        table_name = 'pessoa'

class Grupo(BaseModel):
    dona = ForeignKeyField(column_name='dona_id', field='id', model=Pessoa)
    nome = TextField()

    class Meta:
        table_name = 'grupo'

class Nota(BaseModel):
    criada_em = DateTimeField()
    dona = ForeignKeyField(column_name='dona_id', field='id', model=Pessoa)
    grupo = ForeignKeyField(column_name='grupo_id', field='id', model=Grupo, null=True)
    modificada_em = DateTimeField()
    nota = TextField()
    titulo = TextField()

    class Meta:
        table_name = 'nota'

