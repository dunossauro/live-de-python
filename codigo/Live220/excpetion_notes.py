from sys import platform

class C:
    ...

# e = Exception()
# # print(e.__notes__)

# e.add_note('Blah!')
# e.add_note('Nota 2')
# print(e.__notes__)

# try:
#     1/0
# except Exception as e:
#     e.add_note('Nota1')
#     e.add_note('Nota2')
#     e.add_note('Nota3')
#     raise

try:
    C().batatinha()
except Exception as e:
    if platform == 'linux':
        e.add_note('Batatinha não é disponível para Linux')
        e.add_note('Para linux use fritas()')
    raise e
