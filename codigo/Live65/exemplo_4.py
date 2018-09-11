class ListaBemLoka(list):
    def __add__(self, val):
        """Soma todos os ítens da lista com val"""
        return ListaBemLoka([x + val for x in self])

    def __lshift__(self, val):
        """Fazer append na lista usando <<"""
        self.append(val)

    def __rshift__(self, pos):
        """Remove um item com >>"""
        return self.pop(pos)

    def __neg__(self):
        return ListaBemLoka(reversed(self))
