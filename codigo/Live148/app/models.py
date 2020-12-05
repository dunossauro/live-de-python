import orm
from app.database import database, metadata


class User(orm.Model):
    __tablename__ = "users"
    __database__ = database
    __metadata__ = metadata

    id = orm.Integer(primary_key=True)
    name = orm.String(allow_null=False, max_length=100)
    email = orm.String(allow_null=False, unique=True, index=True, max_length=84)
    password = orm.String(allow_null=False, max_length=255)

    def __repr__(self) -> str:
        return f"Usuario: {self.name}"
