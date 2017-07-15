from pprint import pprint
from sqlalchemy import select
from core import user_table

s = select([user_table])

for row in s.execute():
    pprint(row)
