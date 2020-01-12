from unittest import TestCase
from problemas.problema1 import maior, é_vogal


class TesteProblema1(TestCase):
    def test_maior_0_1_deve_retornar_1(self):
        self.assertEqual(maior(0, 1), 1)
    def test_maior_1_0_deve_retornar_1(self):
        self.assertEqual(maior(1, 0), 1)


class TesteProblema2(TestCase):
    def test_eh_vogal_deve_retornar_vogal_com_entrada_a(self):
        self.assertEqual(é_vogal('a'), 'vogal')
    def test_eh_vogal_deve_retornar_consante_com_entrada_b(self):
        self.assertEqual(é_vogal('b'), 'consoante')
