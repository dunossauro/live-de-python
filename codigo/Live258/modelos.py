from asyncio import run

from sqlalchemy import and_, or_, select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class Model(Base):
    __tablename__ = 'models'

    id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self):
        return f'Model(id={self.id})'


engine = create_async_engine('sqlite+aiosqlite:///database.db', echo=True)


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSession(engine) as s:
        s.add(Model())
        s.add(Model())
        s.add(Model())
        s.add(Model())
        s.add(Model())
        s.add(Model())
        await s.commit()

    async with AsyncSession(engine) as session:
        result = await session.scalars(
            select(Model).where(
                and_(Model.id >= 1, Model.id <= 5), or_(Model.id > 10)
            )
        )
        print(result.all())


run(main())
