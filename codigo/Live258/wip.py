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


Comment(name='dunossauro', comment='LLL', live='youtube')

from sqlalchemy import create_engine, select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

engine = create_async_engine(
    'postgresql+psycopg://app_user:app_password@localhost:5432/app_db',
)

Session = async_sessionmaker(engine)

async def main():
    async with Session() as s:
        result = await s.scalar(
            select(Comment).where(
                Comment.live == 'twitch',
                Comment.name == 'dunossauro',
                Comment.id == 8
            )
        )

        if result:
            await s.delete(result)
            await s.commit()

from asyncio import run

run(main())
