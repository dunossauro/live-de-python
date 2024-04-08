from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

reg = registry()


@reg.mapped_as_dataclass
class Pessoa:
    __tablename__ = 'pessoas'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str]
    email: Mapped[str]
    senha: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, insert_default=func.now()
    )
