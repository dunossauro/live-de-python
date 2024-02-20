# exemplo_09.py
from sqlalchemy import create_engine, inspect

engine = create_engine(
    'postgresql+psycopg://app_user:app_password@localhost:5432/app_db'
)

inspected = inspect(engine)

tables = inspect.get_table_names()
columns = inspected.get_columns('comments')
