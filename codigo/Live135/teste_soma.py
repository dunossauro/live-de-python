from unittest import TestCase
from soma import soma


class TestSoma(TestCase):
    def test_soma(self):
        assert soma(0, 0) == 0
