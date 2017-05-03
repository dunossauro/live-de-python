from unittest import TestCase, main


def soma(x, y):
    return 4


class Testes(TestCase):

    calc = Calc

    def test_soma(self):
        self.assertEqual(self.calc.soma(2, 2), 4)


if __name__ == '__main__':
    main()
