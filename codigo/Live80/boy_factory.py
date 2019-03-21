from factory import Factory, Faker

from serial import Task
from fakes import TaskProvider

Faker.add_provider(TaskProvider)


class TaskFactory(Factory):
    class Meta:
        model = Task

    task_name = Faker('task_name')
    state = Faker('state')
