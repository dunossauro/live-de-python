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
    idade = Column(Integer)

    def __repr__(self):
        return f'Pessoa(nome={self.nome}, idade={self.idade})'


Base.metadata.create_all(engine)


p1 = Pessoa(nome='Eduardo', idade='27')
p2 = Pessoa(nome='Isaias', idade='30')
p3 = Pessoa(nome='Carlos', idade='26')

# session.add(p1)
# session.add(p2)
# session.add(p3)

# session.commit()

from pprint import pprint

pprint(session.query(Pessoa).first())
