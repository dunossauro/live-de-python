from datetime import datetime
from itertools import count
from .database import insert_task, select_tasks

identificador = count()


def process_date(string_date: str):
    return datetime.strptime(string_date, '%d/%m/%Y')


def nova_task(task_name: str, data: str):
    """insere uma nova task na lista de tasks."""
    task = {
        'id': next(identificador),
        'task_name': task_name,
        'date': process_date(data),
        'state': 'TODO'
    }
    result_db = insert_task(task)
    return task


def listar_tasks(task_name: str, state: str = ''):
    return select_tasks(task_name, state)
