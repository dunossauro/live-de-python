# exemplo_10.py
from sqlalchemy import MetaData, Table, create_engine, select

engine = create_engine(
    'postgresql+psycopg://app_user:app_password@localhost:5432/app_db'
)
# engine = create_engine(<URL>)
metadata = MetaData()

comments = Table('comments', metadata, autoload_with=engine)

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
