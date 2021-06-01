from sqlalchemy import (
    Column, Integer, String, update, delete, ForeignKey
)
from sqlalchemy.future import select
from sqlalchemy.orm import (
    declarative_base, sessionmaker, relationship
)
from sqlalchemy.ext.asyncio import (
    create_async_engine, AsyncSession
)

url_do_banco = 'sqlite+aiosqlite:///db.db'

engine = create_async_engine(url_do_banco)

session = sessionmaker(
    engine,
    expire_on_commit=False,
    future=True,
    class_=AsyncSession,
)

Base = declarative_base()


class Pessoa(Base):
    __tablename__ = 'pessoa'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    posts = relationship('Post', backref='pessoa')

    def __repr__(self):
        return f'Pessoa({self.nome})'


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    conteudo = Column(String)
    autor_id = Column(Integer, ForeignKey('pessoa.id'))
    autor = relationship('Pessoa', backref='post')

    def __repr__(self):
        return f'Post({self.titulo})'


async def create_database():
    async with engine.begin() as conn:
        # O que vai rolar quando conectar?
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def criar_pessoa(nome, email):
    # hack: cria pessoa e post
    async with session() as s:
        pessoa = Pessoa(nome=nome, email=email)
        s.add(pessoa)
        post = Post(
            titulo='Live de python',
            conteudo='Segundas as 22:00 hrs',
            pessoa=pessoa,
        )
        s.add(post)

        await s.commit()


async def buscar_pessoa(nome='Felipe'):
    async with session() as s:
        # session.query(Pessoa).filter_by(nome=='Dudu').all()
        query = await s.execute(
            select(Pessoa).where(Pessoa.nome == nome)
        )
        result = query.scalars().all()
        # return query.all()
        # breakpoint()
        return result


async def atualizar_nome(nome_antigo, nome_novo):
    async with session() as s:
        await s.execute(
            update(Pessoa).where(
                Pessoa.nome == nome_antigo
            ).values(nome=nome_novo)
        )
        await s.commit()


async def deletar_pessoa(nome):
    async with session() as s:
        await s.execute(
            delete(Pessoa).where(
                Pessoa.nome == nome
            )
        )
        await s.commit()


async def buscar_post_por_autor(nome):
    async with session() as s:
        query = await s.execute(
            select(Pessoa, Post).join(
                Post.autor
            ).where(
                Pessoa.nome == nome
            )
        )
        result = query.first()
        # result = query.scalar()
        breakpoint()
        return result


from asyncio import run
# run(create_database())
# run(criar_pessoa('Thiago', 'thiago@salgado.com'))
# print(run(atualizar_nome('Thiago', 'Gabriel')))
# print(run(deletar_pessoa('Gabriel')))
print(run(buscar_post_por_autor('Thiago')))
