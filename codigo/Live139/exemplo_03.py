from sqlalchemy import (
    create_engine, Column, Integer, String, ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///test.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship('Pessoa')

    def __repr__(self):
        return f'Produto(nome={self.nome}, pessoa={self.pessoa})'
    


class Pessoa(Base):
    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    produtos = relationship(Produto, backref='pessoas')

    def __repr__(self):
        return f'Pessoa(id={self.id}, nome={self.nome}, idade={self.idade})'


Base.metadata.create_all(engine)


p1 = Pessoa(nome='Eduardo', idade='27')
p2 = Pessoa(nome='Will', idade='27')
pd1 = Produto(nome='Livro', pessoa=p1)
pd2 = Produto(nome='CD', pessoa=p1)
pd3 = Produto(nome='CD', pessoa=p2)

session.add_all([pd1, pd2, p1, p2, pd3])

session.commit()

from pprint import pprint

pprint(session.query(Pessoa).first())
