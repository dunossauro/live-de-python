from sqlalchemy import create_engine, text

engine = create_engine(
    'postgresql+psycopg://app_user:app_password@localhost:5432/app_db',
    echo=True,
)

with engine.connect() as con:
    sql = text('select * from comments limit 10 offset 10')
    result = con.execute(sql)

primeito_valor = result.fetchone()
todos_os_valores = result.fetchall()

print(primeito_valor)
print(todos_os_valores)
