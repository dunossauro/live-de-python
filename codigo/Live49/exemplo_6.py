"""Exemplo usando shelve."""
import shelve

dbm = shelve.open('shelve.pkl')
dbm['dados'] = [1, 2, 3, 4, 5]
dbm['bananas'] = 'bananas'
print(dbm['bananas'])
print(type(dbm['dados']))
