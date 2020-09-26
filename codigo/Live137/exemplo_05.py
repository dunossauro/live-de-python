from pendulum import datetime

dt = datetime(2020, 1, 2)

print(dt.format('dddd DD MMM YYYY', locale='de'))
print(dt.format('dddd DD MMM YYYY', locale='pt-br'))
print(dt.format('dddd DD MMM YYYY', locale='es'))
