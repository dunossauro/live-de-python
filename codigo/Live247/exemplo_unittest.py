from unittest import TestCase
from time import sleep


class TestExample(TestCase):
    def test_short(self):
        sleep(.1)

    def test_mid(self):
        sleep(1)

    def test_mid_long(self):
        sleep(2)

    def test_long(self):
        sleep(3)

    def test_long_long(self):
        sleep(5)
