import re
with open('tabacaria.txt') as _file:
    text = _file.read()

olha = re.search(r'Olha', text)
print(olha)

print(text[olha.start():olha.end()])
