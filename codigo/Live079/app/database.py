
db = []


def insert_task(task: dict):
    ...


def select_tasks(task_name, state):
    if not state:
        return [task for task in db if task_name == task['task_name']]
    return [task for task in db if state == task['state']]
