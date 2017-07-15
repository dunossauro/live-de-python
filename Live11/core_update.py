from sqlalchemy import update
from core import user_table, engine

# datetime.datetime(2017, 7, 3, 20, 20, 17, 134448)
# datetime.datetime(2017, 7, 3, 20, 22, 8, 267343)
conn = engine.connect()

u = update(user_table).where(user_table.c.nome == 'Juacy')

# u = u.values(nome='Juacy')
u = u.values(idade=(user_table.c.idade + 1))

result = conn.execute(u)

print(result.rowcount)

conn.close()
