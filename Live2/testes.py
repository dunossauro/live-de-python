from unittest import TestCase, main


class Calc:
    def soma(self):
        pass


class Testes(TestCase):

    calc = Calc

    def test_soma(self):
        self.assertEqual(self.calc.soma(2, 2), 4)


if __name__ == '__main__':
    main()
