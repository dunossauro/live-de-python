from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///test.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Pessoa(Base):
    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key=True)
    nome = Column(String)


Base.metadata.create_all(engine)

p1 = Pessoa(nome='Fausto')
p2 = Pessoa(nome='Fabio')
p3 = Pessoa(nome='Arnaldo')
p4 = Pessoa(nome='Fernando')
p5 = Pessoa(nome='Leonardo')

session.add(p1)
session.add_all([p2, p3, p4])

# Persiste tudo que estão na sessão
session.commit()


session.add(p5)

# limpa a sessão
session.flush()
