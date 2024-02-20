from sqlalchemy import create_engine

engine_pg = create_engine(
    'postgresql+psycopg://app_user:app_password@localhost:5432/app_db'
)

print(engine_pg.dialect)
print(engine_pg)

engine_lite = create_engine('sqlite:///database.db')

print(engine_lite.dialect)
print(engine_lite)
