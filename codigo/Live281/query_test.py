class T:
    contains: T

class Table:
    field: T
    def filter(*args): ...

def select(*args) -> Table: ...


def list_objects(
    text: str, session: sqlalchemy.orm.Session
) -> list[Table]:
    return session.scalars(
        select(Table)
        .filter(Table.field.contains(text))
    )


def test_list_objects(session):
    # arrange
    session.add_all(
        [
            Table(field='texto', field_a='dummy', field_b='dummy', ...),
            Table(field='texto', field_a='dummy', field_b='dummy', ...),
            Table(field='texto', field_a='dummy', field_b='dummy', ...),
        ]
    )
    session.commit()

    #  act
    list_objects('texto', session)
