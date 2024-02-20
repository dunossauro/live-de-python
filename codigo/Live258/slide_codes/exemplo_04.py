from sqlalchemy import create_engine, text

engine = create_engine(
    'postgresql+psycopg://app_user:app_password@localhost:5432/app_db',
    echo=True,
)


with engine.connect() as connection:
    sql = text('select id, name, comment from comments')
    result = connection.execute(sql)
