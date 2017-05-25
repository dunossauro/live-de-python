from numbers import Number
from unittest import TestCase, main
import operator


def validate(func, cache={}):
    """
    Decorador de cache.

    Args:
        - func: Função decorada
        - cache: dicionário que armazena um único valor para cache

    Return: check_replace
    """
    def check_replace(x, y=None):
        """
        Faz a checagem da validade da estrada das funções.

        Args:
            - x: primeiro valor passado pela função
            - y: None: passado opcionamente para a função decorada
                Caso não seja passado o valor None será substituido pelo cache

        Return: func executada com o cache
        """
        if not y:
            y = cache['value']
        if isinstance(x, Number) and isinstance(y, Number):
            cache['value'] = func(x, y)
            return cache['value']
        raise Exception('Entrada incorreta, use numeros')
    return check_replace


@validate
def soma(x, y, op=operator.add):
    return op(x, y)


@validate
def sub(x, y, op=operator.sub):
    return op(x, y)


@validate
def div(x, y, op=operator.floordiv):
    return op(x, y)


@validate
def mul(x, y, op=operator.mul):
    return op(x, y)


class Testes_calculadora(TestCase):

    def test_soma(self):
        self.assertEqual(soma(2, 2), 4)

    def test_soma_neg(self):
        self.assertEqual(soma(-2, -3), -5)

    def test_soma_float(self):
        self.assertEqual(soma(2.0, 1.0), 3.0)

    def test_sub(self):
        self.assertEqual(sub(2, 2), 0)

    def test_sub_float(self):
        self.assertEqual(sub(2.0, 2.0), 0)

    def test_soma_string(self):
        with self.assertRaises(Exception):
            soma('Eduardo', 'jaber')

    def test_sub_string(self):
        with self.assertRaises(Exception):
            sub('Eduardo', 'jaber')

    def test_mul(self):
        self.assertEqual(mul(3, 3), 9)

    def test_mul_string(self):
        with self.assertRaises(Exception):
            mul(3, 'Eduardo')

    def test_div(self):
        self.assertEqual(div(3, 3), 1)

    def test_div_string(self):
        with self.assertRaises(Exception):
            div(3, 'Eduardo')

    def test_cache_soma(self):
        self.assertEqual(soma(soma(2, 2)), 8)

    def test_cache_sub(self):
        """
        Explicação.

        Na primeira subtração 10 - 5 o reusltado é 5

        cache - resultado == 0
        """
        self.assertEqual(sub(sub(10, 5)), 0)


if __name__ == '__main__':
    main()
