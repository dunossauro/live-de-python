from unittest import TestCase, main

from calculator import soma, invert, sum_, is_number, check_numbers


class SomaTests(TestCase):
    def test_soma(self):
        self.assertEqual(soma(10, 10), 20)


class InvertTests(TestCase):
    def test_invert(self):
        self.assertEqual(invert(5), -5)


class SumTests(TestCase):
    def test_sum(self):
        self.assertEqual(sum_(1, 2, 3, 4), 10)


class Is_numberTests(TestCase):
    def test_is_number(self):
        self.assertEqual(is_number(1), True)


class Check_numbersTests(TestCase):
    def test_check_numbers(self):
        self.assertEqual(check_numbers(1, 'a'), False)


if __name__ == '__main__':
    main()
