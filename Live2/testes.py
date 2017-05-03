from unittest import TestCase, main


def soma(x, y):
    return 4


class Testes(TestCase):

    def test_soma(self):
        self.assertEqual(soma(2, 2), 4)


if __name__ == '__main__':
    main()
