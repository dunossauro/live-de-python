from unittest import TestCase, main
from serial import Task, task_serializer, dump_db
from fakes import faker
from boy_factory import TaskFactory


class TestModelTask(TestCase):
    def test_check_model_representation(self):
        esperado = 'Task(task_name="Acordar", state="TODO")'
        chamada = Task('Acordar', 'TODO')

        self.assertEqual(esperado, str(chamada))

    def test_check_model_has_id_and_his_is_int(self):
        chamada = Task('', '')
        self.assertIsInstance(chamada.id_, int)



class TestTaskSerializer(TestCase):
    def test_task_serializer_deve_ser_um_dict(self):
        task_name = 'Ligar para o Will'
        state = 'TODO'

        task = Task(task_name, state)

        self.assertIsInstance(task_serializer(task), dict)

    def test_task_serializer_nao_deve_serializar_um_tipo_nao_task(self):
        task_name = 'Ligar para o Will'

        with self.assertRaises(AttributeError):
            task_serializer(task_name)


class TestDumpDB(TestCase):
    def test_serializer_deve_transformar_todos_os_dados_em_dicionarios(self):
        fake_tasks = TaskFactory.create_batch(10)
        results = dump_db(fake_tasks, task_serializer)

        for r in results:
            with self.subTest(r=r):
                self.assertIsInstance(r, dict)


if __name__ == '__main__':
    main()
