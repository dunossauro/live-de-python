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

    def __repr__(self) -> str:
        return f'Comment({self.id=}, {self.name=}, {self.comment=}, {self.live=}, {self.created_at=})'


Comment(name='dunossauro', comment='LLL', live='youtube')

# from sqlalchemy import create_engine, select

# engine = create_engine(
#     'postgresql+psycopg://app_user:app_password@localhost:5432/app_db'
# )

# from sqlalchemy.orm import Session

# with Session(engine) as s:
#     result = s.scalars(select(Comment))
#     print(result.fetchmany(3))
