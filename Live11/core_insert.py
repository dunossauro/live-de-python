from core import user_table, engine

conn = engine.connect()

ins = user_table.insert()

new_user = ins.values(nome='Juacy',
                      idade=28,
                      senha='souzapereira')

conn.execute(new_user)

# conn.execute(user_table.insert(), [
#     {'nome': 'Marivaldo', 'idade': 35, 'senha': 'gatinho_123'},
#     {'nome': 'Jean', 'idade': 19, 'senha': 'jeanzinho_123'},
#     {'nome': 'Juancy', 'idade': 27, 'senha': 'souzapereira'},
#     {'nome': 'Luciana', 'idade': 25, 'senha': 'gatinha_luluzinha'}
# ])
