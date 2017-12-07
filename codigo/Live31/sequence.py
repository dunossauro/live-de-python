from collections.abc import Container, Iterable, Sized


class Sequence(Container, Iterable, Sized):
    def __init__(self, sequence):
        self.seq = sequence

    def __contains__(self, val):
        return val in self.seq

    def __iter__(self):
        return iter(self.seq)

    def __len__(self):
        return len(self.seq)
