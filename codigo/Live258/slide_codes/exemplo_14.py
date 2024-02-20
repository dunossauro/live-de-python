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

    def __repr__(self) -> str:
        return f'Comment({self.id=}, {self.name=}, {self.comment=}, {self.live=}, {self.created_at=})'


Comment(name='dunossauro', comment='LLL', live='youtube')

from sqlalchemy import create_engine, select

engine = create_engine(
    'postgresql+psycopg://app_user:app_password@localhost:5432/app_db'
)

from sqlalchemy.orm import Session

with Session(engine) as s:
    result = s.scalars(select(Comment))
    print(result.fetchmany(3))
