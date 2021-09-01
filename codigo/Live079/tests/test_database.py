from unittest import TestCase, mock
from app.database import select_tasks

tasks = [
    {'id': 1, 'task_name': 'Dormir', 'date': '??', 'state': 'TODO'},
    {'id': 2, 'task_name': 'Acordar', 'date': '??', 'state': 'TODO'},
    {'id': 3, 'task_name': 'Ligar pro will', 'date': '??', 'state': 'TODO'},
    {'id': 4, 'task_name': 'Acordar', 'date': '??', 'state': 'TODO'},
    {'id': 5, 'task_name': 'Acordar', 'date': '??', 'state': 'Fazendo'},
]


class TestSelectTasks(TestCase):
    @mock.patch('app.database.db', new=tasks)
    def test_select_tasks_deve_retornar_somente_tasks_de_acordar(self):
        results = select_tasks('Acordar', '')

        for result in results:
            with self.subTest(f'Acordar in {result}'):
                self.assertEqual('Acordar', result['task_name'])

    @mock.patch('app.database.db', new=tasks)
    def test_select_tasks_deve_retornar_somente_tasks_com_state_fazendo(self):
        results = select_tasks('', 'Fazendo')

        for result in results:
            with self.subTest(f'Acordar in {result}'):
                self.assertEqual('Fazendo', result['state'])
