"""
{id: <int>, task_name: <str>, state: <str>}
"""


class Task:
    """Uma classe típica de orms."""

    def __init__(self, task_name, state, id_: int = 0):
        self.id_ = id_
        self.task_name = task_name
        self.state = state

    def __repr__(self):
        return f'Task(task_name="{self.task_name}", state="{self.state}")'


def task_serializer(task: Task) -> dict:
    return {
        'task_name': task.task_name,
        'state': task.state,
    }


def dump_db(db, serializer):
    return [serializer(obj) for obj in db]
