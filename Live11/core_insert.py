from core import users_table, engine

conn = engine.connect()

"""
Inserir um único registro.

users_table: Exatamente a tabela que criamos
"""
ins = users_table.insert()

new_user = ins.values(nome="Fábio",
                      idade=35,
                      senha="huuhsp")

conn.execute(new_user)

"""
Criando uma conexão com o banco.

conn: conexão
execute: executa uma série de ações. Caso seja passado um array
    ele funciona como um functor
"""

conn.execute(users_table.insert(), [
    {"nome": "Juacy", "idade": 30, "senha": "dink"},
    {"nome": "Pedro", "idade": 25, "senha": "nippon"},
    {"nome": "Paulo", "idade": 40, "senha": "macaca"}
])
