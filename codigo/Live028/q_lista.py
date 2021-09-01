from collections import deque


class Lista:
    def __init__(self):
        self.lista = deque()

    def insere(self, val, pos=None):
        if pos:
            self.lista.insert(val, pos)
        else:
            self.lista.append(val)

    def remove(self, val):
        return self.lista.remove(val)

    def __repr__(self):
        return 'Lista [{}]'.format(', '.join(str(x) for x in self.lista))
