# SQLAlchemy

- Iniciado em 2005, primeira release 2006
- Criado por Mike Byers
- Atualmente na versão 2.0.27

## Uma introdução

O SQLAlchemy é um kit de ferramentas para trabalhar com bancos de dados SQL e Python. A ideia principal do sqlalchemy é "abstrair" as chamadas diretas para drivers específicos de bancos de dados. Que tem suas peculiaridades específicas. Além de poder alterar entre banco de dados com a facilidade da API permanece a mesma.

O toolkit suporta:

- async e sync
- Anotações de tipos e forma dinâmica
- Implementa a DBAPI ([PEP 249](https://peps.python.org/pep-0249/))
- Suporta Cpython e PyPy

O SQLAlchemy é dividido em duas partes especiais. O Core e o ORM:

![Camadas](https://docs.sqlalchemy.org/en/20/_images/sqla_arch_small.png){: .center .shadow }

### Instalação

Estamos a um pip install de distância do sqlalchemy:

```bash
pip install sqlalchemy
```

Também vamos usar outros pacotes durante esse tutorial para exemplos:

```bash
pip install aiolite  # vamos usar o sqlite async em algum momento
pip install psycopg-binary  # para mostrar a diferença quando usamos postgres
```

## Core

O core é o componente mais básico do SQLAlchemy. Responsável por criar a conexão com o banco de dados, fazer buscas e definir tipos. Alguns componentes importantes são:

- **Engine**
  - Connection: Interface para se comunicar com o banco
  - Result: Objeto de resultado das operações
  - Dialect: Mecanismos específicos para cada banco de dados
  - connection **Pool**: Deixa conexões em memória para ser mais fácil reutilizar
- **SQL Expression Language**: Construções em Python para representar SQL
- **Schema/Types**: Construções em python que representam tabelas, colunas e tipos de dados

### Engine

A engine, o coração do Alchemy, é uma [fábrica](https://refactoring.guru/design-patterns/abstract-factory) de conexões com o banco de dados. O objetivo dela é que de forma dinâmica podemos nos comunicar com diferentes drivers de banco de dados usando dialetos específicos para cada banco de dados.

Funcionando da seguinte forma:

```mermaid
flowchart LR
  engine --> dialeto
  dialeto --> DBAPI
  DBAPI --> DB[Banco de dados]
```

Em código:

```python
# exemplo_00.py
from sqlalchemy import create_engine


engine = create_engine(
    'sqlite:///database.db'
)

print(engine)
```

### Dialetos

A engine fabrica uma conexão com a base de dados específica usando os dialetos. Dialetos são chamadas diretas para os drivers específicos para databases específicos.

Por exemplo, o SQLAlchemy suporta nativamente:

- SQLite
- PostgreSQL
- MySQL / MariaDB
- Oracle
- Microsoft SQL Server

Contando com diversas implementações via [plugins](https://docs.sqlalchemy.org/en/20/dialects/index.html#external-dialects) como CockroachDB, Firebird, Amazon Redshift, etc..

Um exemplo usando postgres e sqlite:

```python
# exemplo_00.py
from sqlalchemy import create_engine


engine_pg = create_engine(
    'postgresql+psycopg://app_user:app_password@localhost:5432/app_db'
)

print(engine_pg.dialect)
# <sqlalchemy.dialects.postgresql.psycopg.PGDialect_psycopg object at 0x70f32a4ce6f0>
print(engine_pg)

engine_lite = create_engine('sqlite:///database.db')

print(engine_lite.dialect)
# <sqlalchemy.dialects.sqlite.pysqlite.SQLiteDialect_pysqlite object at 0x70f329aa7560>
print(engine_lite)
```

### Connection

Após a escolha de um dialeto específico, precisamos nos comunicar com uma base de dados, nos conectar ao banco:

```python
# exemplo_01.py
from sqlalchemy import create_engine


engine = create_engine('sqlite://')

connection = engine.connect()  # Cria uma conexão
connection.close()  # Finaliza a conexão
```

#### DBAPI
Essa conexão vai até o driver específico do banco de dados usando a DBAPI.

```python
from sqlalchemy import create_engine


engine = create_engine(
    'sqlite:///database.db',
    echo=True,
)

connection = engine.connect()
print(connection.connection.dbapi_connection)
# <sqlite3.Connection object at 0x747eb38e8f40>

print(connection.connection.driver_connection)
# <sqlite3.Connection object at 0x747eb38e8f40>

connection.close()
```

### Pool

Uma instrução relativamente cara de IO é criação da conexão com o banco de dados. Por esse motivo, o sqlalchemy armazena as conexões em um `reservatório` de conexões. Chamamos de `Pool`.

Quando uma conexão é fechada, ela é fechada no contexto do sqlalchemy, mas se mantém aberta na pool. Dessa forma o escalonamento acontece de forma transparente. Quando novas conexões forem abertas, caso existam conexões no pool, elas serão atribuídas.


```python
# Exemplo_02.py
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
```

### Transações

Com a conexão estabelecida, podemos executar as transações. As transações são feita pela conexão usando o método `.execute()`.

Para simplificar, por agora vamos executar um SQL puro com a função `text`:

```python
# exemplo_03.py
from sqlalchemy import create_engine, text

engine = create_engine(<URL>, echo=True)

connection = engine.connect()

sql = text('select id, name, comment from comments')

print(sql)
# select id, name, comment from comments  --> print(sql)

result = connection.execute(sql)

"""
INFO sqlalchemy.engine.Engine BEGIN (implicit)  # Começou a tansação
INFO sqlalchemy.engine.Engine select id, name, comment from comments  # Executou o select
INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}  # log
INFO sqlalchemy.engine.Engine ROLLBACK  # Fez rollback
"""

connection.close()
```

```python
from sqlalchemy import create_engine, text

engine = create_engine(
    'postgresql+psycopg://app_user:app_password@localhost:5432/app_db',
    echo=True,
)


with engine.connect() as connection:
    sql = text('select id, name, comment from comments')
    result = connection.execute(sql)
```

#### Result
O resultado obtido no execute é um objeto especial do sqlalchemy chamado `Result`. Result implementa diversos métodos, além de ser um iterável.

Alguns dos métodos que gostaria de mostrar do result:

- .fetchone(): pega o primeiro
- .fetchmany(3) / .partitions(3): pega alguns valores
- .fetchall() / .all(): pega todos os valores
- .first(): Pega 1, mas não dá erro se não conseguir

```python
# exemplo_07.py
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

```

### Schemas / Types

Os metadados das tabelas podem ser descritos por Schemas e seus determinados tipos.

```python
import sqlalchemy as sa

meta = MetaData()

t = sa.Table('comments', meta,
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('comment', sa.String(), nullable=False),
    sa.Column('live', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
)
```

#### Reflection

O SQLAlchemy conta com um mecanismo de inspeção de metadados:

```python
# exemplo_09.py
from sqlalchemy import create_engine, inspect

engine = create_engine('url')

inspected = inspect(engine)

tables = inspect.get_table_names()
columns = inspected.get_columns('comments')
```

Essas funções podem ser agregadas a construção de schemas, para evitar a criação dos metadados em um banco que já existe:

```python
# exemplo_10.py
from sqlalchemy import create_engine, Table, MetaData

engine = create_engine(
    'postgresql+psycopg://app_user:app_password@localhost:5432/app_db'
)
# engine = create_engine(<URL>)
metadata = MetaData()

comments = Table('comments', metadata, autoload_with=engine)

print(comments.c)
print(comments.columns)
print(comments.c.id)
```

### SQL Expression Language

Até esse momento, todas as operações que fizemos com o banco, fizemos com a função `text` e escrevemos SQL na mão.

O Core tem um grupo de funções e objetos que podem nos ajudar a montar sql tanto para DQL(Data Query Language), quanto para DML(Data Manipulation Language). Usado em conjunto com os Schemas.

#### DQL - Query Builder

Uma das partes mais importantes dentro dos bancos de dados é a busca pelos dados. O que chamamos de Query. O Alchemy tem um sistema completo e extenso sobre a criação de queries.

Começaremos belo básico, a função `select()`

```python
with engine.connect() as con:
    stmt = select(comments)
    print(stmt)
```

Até

```python
with engine.connect() as con:
    stmt = (
        select(comments)
        .where(
            (
                (comments.c.name == 'Eduardo Mendes')
                | (comments.c.name == 'dunossauro')
            )
            & ((comments.c.live == 'youtube') | (comments.c.live == 'twitch'))
        )
        .limit(3)
        .offset(0)
        .order_by(comments.c.id)
    )
    print(stmt)

    result = con.execute(stmt)
    print(result.all())
```



#### DML

Quando precisamos manipular dados no sql, usamos algumas das instruções listadas:

- delete: remove registros
- insert: insere registros
- update: atualiza registos

O Alchemy tem uma função específica para cada uma dessas operações.

```python
with engine.connect() as con:
    with con.begin():
        stmt = insert(comments).values(
            name='dunossauro',
            comment='LLL',
            live='youtube',
            created_at=datetime.now(),
        )
        con.execute(stmt)

    with con.begin():
        stmt = (
            update(comments)
            .where(
                comments.c.name == 'dunossauro',
                comments.c.comment == 'LLL',
                comments.c.live == 'youtube',
            )
            .values(comment='Pei')
        )

        con.execute(stmt)

    with con.begin():
        stmt = select(comments).where(
            comments.c.name == 'dunossauro',
            comments.c.live == 'youtube',
            comments.c.comment == 'Pei',
        )
        results = con.execute(stmt)
        print(results.all())

    with con.begin():
        stmt = delete(comments).where(
            comments.c.name == 'dunossauro',
            comments.c.live == 'youtube',
            comments.c.comment == 'Pei',
        )
        con.execute(stmt)

    with con.begin():
        stmt = select(comments).where(
            comments.c.name == 'dunossauro',
            comments.c.live == 'youtube',
            comments.c.comment == 'Pei',
        )
        results = con.execute(stmt)
        print(results.all())
```


## ORM

ORM é construído no topo do [Core](#core)

- Mapeamento: Relaciona objetos python (classes) com tabelas do banco de dados
- Unit Of Work: Persiste e atualiza os objetos no banco de dados usando o padrão
- xSEL: Estende o formato do core para a linguagem de expressão do core usando objetos
- Converte linhas das tabelas em objetos definidos no mapeamento
- Prove um sistema de relacionamentos entre os objetos
- Sincroniza o estado dos objetos em transações com banco de dados

### Objetos

A parte interessante de um ORM é poder definir os schemas usando objetos do python

```python
from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    ...

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    comment = Column(String, nullable=False)
    live = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
```

#### Typing?

Por que não?

```python
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class Comment(Base):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    comment: Mapped[str]
    live: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
```

#### Dataclasses?

```python
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

reg = registry()


@reg.mapped_as_dataclass
class Comment:
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    comment: Mapped[str]
    live: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
```

#### Modelos imperativos


```python
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    PrimaryKeyConstraint,
    String,
    Table,
)
from sqlalchemy.orm import registry

mapper_registry = registry()

t = Table('comments', mapper_registry.metadata,
    Column('id', Integer(), nullable=False),
    Column('name', String(), nullable=False),
    Column('comment', String(), nullable=False),
    Column('live', String(), nullable=False),
    Column('created_at', DateTime(), nullable=True),
    PrimaryKeyConstraint('id'),
)

class Comment:
    pass

mapper_registry.map_imperatively(Comment, t)
```

#### Automap

https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#automating-column-naming-schemes-from-reflected-tables

### Sessão

## Referências

### PEPs

PEP 249 – Python Database API Specification v2.0: https://peps.python.org/pep-0249/

### Documentação

Documentação oficial: https://www.sqlalchemy.org/

### Vídeos

Palestra do Mike Byers na Python web conf (2021): https://youtu.be/1Va493SMTcY

### Blogs

Mike Byers - Patterns Implemented by SQLAlchemy: https://techspot.zzzeek.org/2012/02/07/patterns-implemented-by-sqlalchemy/
