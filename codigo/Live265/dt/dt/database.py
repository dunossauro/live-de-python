from datetime import datetime

from sqlalchemy import create_engine, func
from sqlalchemy.orm import Mapped, mapped_column, registry, sessionmaker

reg = registry()

engine = create_engine(
    'postgresql+psycopg://app_user:app_password@elefante:5432/app_db'
)
Session = sessionmaker(engine)


def get_session():
    with Session() as s:
        yield s


@reg.mapped_as_dataclass
class Task:
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    task_name: Mapped[str]
    task_desc: Mapped[str]
    status: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, default_factory=func.now
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, default_factory=func.now
    )
