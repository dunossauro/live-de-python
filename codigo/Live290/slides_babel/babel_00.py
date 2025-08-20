from babel import Locale

locale = Locale('pt', 'BR')

print(locale.display_name)  # Português (Brasil)
print(locale.territory_name) # Brasil

l2 = Locale.parse('pt')
print(l2.display_name) # Português
