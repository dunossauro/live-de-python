from random import choice
from faker import Faker
from faker.providers import BaseProvider

from serial import Task


class TaskProvider(BaseProvider):
    """Modelo para prover tasks."""

    def task_name(self):
        tasks = ['Acordar', 'Dormir', 'Trabalhar', 'Fazer a live', 'Codar']
        return choice(tasks)

    def state(self):
        states = ['TODO', 'DOING', 'DONE']
        return choice(states)

    def id_(self):
        return self.random_int(0, 999)

    def Task(self):
        return Task(self.task_name(), self.state(), self.id_())


faker = Faker()
faker.add_provider(TaskProvider)
