# exemplo_10.py
from sqlalchemy import MetaData, Table, create_engine

engine = create_engine(
    'postgresql+psycopg://app_user:app_password@localhost:5432/app_db'
)
# engine = create_engine(<URL>)
metadata = MetaData()

comments = Table('comments', metadata, autoload_with=engine)

print(comments.c)
print(comments.columns)
print(comments.c.id)
