from pendulum import set_locale, now

set_locale('pt-br')
n = now('UTC')

print(n.add(years=2).diff_for_humans())
