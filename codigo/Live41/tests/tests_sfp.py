"""SFP tests."""

from unittest import TestCase, main
from sfp import *


class testHead(TestCase):
    def test_should_get_first_element_to_list(self):
        self.assertEqual(head([1, 2, 3, 4]), 1)
        self.assertEqual(head([2, 3, 4, 1]), 2)

    def test_should_get_first_element_to_iterable(self):
        result = head(iter([1, 2, 3, 4]))
        self.assertEqual(result, 1)


class testLast(TestCase):
    def test_should_get_last_element_to_list(self):
        self.assertEqual(last([1, 2, 3, 4]), 4)

    def test_should_get_last_element_to_iterable(self):
        result = last(iter([1, 2, 3, 4]))
        self.assertEqual(result, 4)


class testNuber(TestCase):
    def test_should_um(self):
        self.assertEqual(number(1), 'Um')

    def test_should_sete(self):
        self.assertEqual(number(7), 'sete')

    def test_should_none(self):
        self.assertEqual(number(99), 'Não sei resolver')


if __name__ == '__main__':
    main()
