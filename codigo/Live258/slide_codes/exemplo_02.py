from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db')

print(engine.pool)
# <sqlalchemy.pool.impl.QueuePool object at 0x73261435c770>

con_1 = engine.connect()

print(engine.pool.status())
# Pool size: 5  Connections in pool: 0 Current Overflow: -4 Current Checked out connections: 1

con_2 = engine.connect()

print(engine.pool.status())
# Pool size: 5  Connections in pool: 0 Current Overflow: -2 Current Checked out connections: 2

con_1.close()

print(engine.pool.status())
# Pool size: 5  Connections in pool: 1 Current Overflow: -3 Current Checked out connections: 1

con_3 = engine.connect()
print(engine.pool.status())
# Pool size: 5  Connections in pool: 0 Current Overflow: -3 Current Checked out connections: 2
