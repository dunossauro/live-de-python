from unittest import TestCase, mock
from app.todo import nova_task, process_date, listar_tasks
from datetime import datetime

"""
{
    'id': int,
    'task_name': str,
    'date': datetime.datetime,
    'state': str['TODO', 'Fazendo', 'Pronto']
}

"""

class TestNovaTask(TestCase):
    def test_nova_task(self):
        esperado = {
            'id': 1,
            'task_name': 'Ligar pro Will',
            'date': datetime(2019, 2, 19, 0, 0, 0),
            'state': 'TODO'
        }
        result = nova_task('Ligar pro Will', '19/02/2019')

        self.assertEqual(esperado, result)

    @mock.patch('app.todo.process_date', return_value=123)
    def test_process_date_deve_ser_chamado_com_19_02_2019(self, mocked):
        # chama a função
        result = nova_task('', '19/02/2019')

        # Garante que a função interna foi chamada
        mocked.assert_called_with('19/02/2019')

        # Garantir se o resultado está no contexto
        self.assertEqual(result['date'], 123)

    @mock.patch('app.todo.insert_task')
    def test_insert_task_deve_chamado_com_o_objeto_da_task(self, mocked):
        # chama a função
        result = nova_task('Ligar pro Will', '19/02/2019')

        mocked.assert_called_with(result)

class TestProcessDate(TestCase):
    def test_process_date_deve_converter_para_datetime_a_string_passada(self):
        esperado = datetime(
            2019, 2, 19, 0, 0, 0
        )

        result = process_date('19/02/2019')

        self.assertEqual(esperado, result)


class TestListarTasks(TestCase):
    ...
