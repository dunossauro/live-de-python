from sqlalchemy import create_engine, MetaData, Column, Table, Integer, String


engine = create_engine('sqlite:///lista.db',
                       echo=False)

metadata = MetaData(bind=engine)

episodios = Table('episodios', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('temporada', Integer),
                  Column('episodio', Integer),
                  Column('nome', String(40)))

metadata.create_all()
