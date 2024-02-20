from asyncio import run

from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine(
    'postgresql+psycopg://app_user:app_password@localhost:5432/app_db',
    echo=True,
)


async def main():
    async with engine.connect() as connection:
        sql = text('select id, name, comment from comments')
        result = await connection.execute(sql)


run(main())
