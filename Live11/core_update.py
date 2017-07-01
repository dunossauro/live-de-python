from sqlalchemy import update
from core import users_table, engine

conn = engine.connect()

u = update(users_table).where(users_table.c.nome == "Juacy")

u = u.values(idade=(users_table.c.idade + 1))

result = conn.execute(u)

print(result.rowcount)
