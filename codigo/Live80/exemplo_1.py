from faker import Faker

faker = Faker('pt_BR')

d = {
    'name': faker.name()
}

# explorar instancia de faker

print(d)
