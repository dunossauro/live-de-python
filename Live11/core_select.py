from sqlalchemy import select
from core import users_table

s = select([users_table])
result = s.execute()

for row in result:
    print(row)
