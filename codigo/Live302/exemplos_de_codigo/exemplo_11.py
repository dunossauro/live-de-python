class Contexto:

    def __init__(self, exc=ZeroDivisionError):
        self.exc = exc

    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is self.exc:
            return True

with Contexto(NameError):
    a + 1
