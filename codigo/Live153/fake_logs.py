from faker import Faker
fake = Faker()

log = open('logs.csv', 'w')

log.write('data,ampm,bool,nome,telefone,email\n')


for _ in range(100):
    log.write(','.join([
        fake.date_time_this_decade().strftime('%m/%d/%Y'),
        fake.am_pm(),
        str(fake.pybool()),
        fake.name(),
        fake.bothify(text='??-#########', letters='123456789'),
        fake.ascii_company_email()
    ]) + '\n')
