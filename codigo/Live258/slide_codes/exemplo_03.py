from sqlalchemy import create_engine, text

engine = create_engine(
    'postgresql+psycopg://app_user:app_password@localhost:5432/app_db',
    echo=True,
)

connection = engine.connect()

sql = text('select id, name, comment from comments')

print(sql)
# select id, name, comment from comments


result = connection.execute(sql)
"""
INFO sqlalchemy.engine.Engine BEGIN (implicit)  # Começou a tansação
INFO sqlalchemy.engine.Engine select id, name, comment from comments  # Executou o select
INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}  # log
INFO sqlalchemy.engine.Engine ROLLBACK  # Fez rollback
"""

connection.close()
