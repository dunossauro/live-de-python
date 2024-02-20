from sqlalchemy import create_engine

engine = create_engine('sqlite://')

connection = engine.connect()

connection.close()
