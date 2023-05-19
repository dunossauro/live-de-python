from exemplo_01 import Person, Todo, Session, engine
from factory import Factory, Faker
from factory.fuzzy import FuzzyChoice


class PersonFactory(Factory):
    class Meta:
        model = Person

    name = Faker('name', locale='pt_BR')


class TodoFactory(Factory):
    class Meta:
        model = Todo

    title = FuzzyChoice(
        ['Acordar', 'Dormir', 'Tomar Banho', 'Ligar para chefe',
         'Fazer almoço', 'Lavar louça', 'Pendurar roupa', 'Sair com crush',
         'Ir para o trabalho', 'Escrever o relatório', 'Terminar commit',
         'Vizitar vovó', 'Ir para academia', 'Dizer que te amo',
         'Assistir a Live de Python', 'Comprar um sapato', 'Assistir Dr. House',
         'Fazer exercício', 'Limpar a geladira', 'Fazer compras',
         'Pedir aquela pizza', 'Platinar marvel vs. capcom', 'Baixar pokémons']
    )
    status = FuzzyChoice(['todo', 'doing', 'done'])
    person_id = Faker('pyint', min_value=1, max_value=10)


with Session(engine) as s:

    for p in PersonFactory.create_batch(10):
        s.add(p)
        s.commit()

    for p in TodoFactory.create_batch(100):
        s.add(p)
        s.commit()
