from typing import override


class BaseForm:
    def area(self):
        ...


class Cicle(BaseForm):
    @override
    def area(self):
        ...


class Square(BaseForm):
    @override
    def area(self):
        ...


class Error(BaseForm):
    @override
    def teste(self):
        ...
