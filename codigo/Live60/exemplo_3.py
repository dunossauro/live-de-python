try:
    f = open('arquivo.txt')
except FileNotFoundError:
    print('Arquivo não existe')
else:
    print(f.read())
    f.close()
finally:
    print('Vou executar com erro ou sem')
