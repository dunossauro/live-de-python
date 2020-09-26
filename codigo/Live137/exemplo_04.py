from pendulum import parse

p1 = parse('2020-09-07T22:55:20Z/2020-09-12T22:55:20Z')

for day in p1.range('days'):
    print(day)


p2 = parse('2020-09-07T22:55:20Z/2025-09-07T22:55:20Z')

for year in p2.range('years'):
    print(year)
