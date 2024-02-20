from sqlalchemy import create_engine, text

engine = create_engine(
    'postgresql+psycopg://app_user:app_password@localhost:5432/app_db',
    echo=True,
)

query = 'select id, name, comment from comments limit 10 offset {of}'

with engine.connect() as connection:
    with connection.begin():
        sql = text(query.format(of=0))
        result1 = connection.execute(sql)
    with connection.begin():
        sql = text(query.format(of=1))
        result2 = connection.execute(sql)
    with connection.begin():
        sql = text(query.format(of=2))
        result3 = connection.execute(sql)
