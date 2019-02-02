from unittest import TestCase
from app.fila import Fila


class TestFila(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.arquivo = 'arquivo.txt'
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
        from os import remove
        remove(cls.arquivo)

    def setUp(self):
        self.fila = Fila()
        print('setup')

    def test_cria_arquivo(self):
        open(self.arquivo, 'w')

    def tearDown(self):
        print('tearDown')

    def test_1_quando_5_entrar_na_fila_5_deve_estar_no_final_da_fila(self):
        entrada = 5
        saida_esperada = 5

        # quando 5 entrar na fila
        self.fila.entrar(entrada)

        # então 5 deve estar na fila
        self.assertEqual(saida_esperada, self.fila[-1])
        print(self.fila)
        # print('test_quando_5_entrar_na_fila_5_deve_estar_no_final_da_fila')

    def test_quando_10_entrar_na_fila_10_deve_estar_no_final_da_fila(self):
        entrada = 10
        saida_esperada = 10

        # quando 10 entrar na fila
        self.fila.entrar(entrada)

        # então 10 deve estar na fila
        self.assertEqual(saida_esperada, self.fila[-1])
        print(self.fila)
        # print('test_quando_10_entrar_na_fila_10_deve_estar_no_final_da_fila')

    def test_quando_10_entrar_na_fila_seguido_de_5_10_deve_estar_no_comeco_da_fila(self):
        entrada1 = 10
        entrada2 = 5

        saida_esperada = 10

        self.fila.entrar(entrada1)
        self.fila.entrar(entrada2)

        self.assertEqual(saida_esperada, self.fila[0])
        print(self.fila)
        # print('test_quando_10_entrar_na_fila_seguido_de_5_10_deve_estar_no_comeco_da_fila')
