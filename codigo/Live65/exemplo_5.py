class ListaBemLoka:
    def __init__(self, l):
        self.l = l or []

    def __add__(self, val):
        """Soma todos os ítens da lista com val"""
        return ListaBemLoka([x + val for x in self.l])

    def __lshift__(self, val):
        """Fazer append na lista usando <<"""
        self.l.append(val)

    def __rshift__(self, pos):
        """Remove um item com >>"""
        return self.l.pop(pos)

    def __neg__(self):
        return ListaBemLoka(reversed(self.l))

    def __iadd__(self, val):
        """Soma todos os ítens da lista com val e manter no obj"""
        self.l = [x + val for x in self.l]
