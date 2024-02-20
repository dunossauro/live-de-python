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

t = Table(
    'comments',
    mapper_registry.metadata,
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
