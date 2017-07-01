from sqlalchemy import delete
from core import users_table, engine

conn = engine.connect()

u = delete(users_table).where(users_table.c.nome == "Juacy")
result = conn.execute(u)

print(result.rowcount)
