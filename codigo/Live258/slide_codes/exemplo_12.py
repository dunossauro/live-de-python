# exemplo_10.py
from datetime import datetime

from sqlalchemy import (
    MetaData,
    Table,
    create_engine,
    delete,
    insert,
    select,
    update,
)

engine = create_engine(
    'postgresql+psycopg://app_user:app_password@localhost:5432/app_db'
)
# engine = create_engine(<URL>)
metadata = MetaData()

comments = Table('comments', metadata, autoload_with=engine)

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
