from unittest import TestCase
from app.app import converte_F_para_C, converte_C_para_F


class TestConverteFParaC(TestCase):

    def test_do_zé(self):
        valores = [(32, 0), (-40, -40)]

        for input_, output in valores:
            with self.subTest(input_=input_, output=output):
                self.assertEqual(
                    converte_F_para_C(input_),
                    output
                )
    
    def test_deve_retornar_0_quando_receber_32(self):
        assert converte_F_para_C(32) == 0

    def teste_deve_retornar__40_quando_receber__40(self):
        assert converte_F_para_C(-40) == -40

    def test_deve_retornar__17_77_quando_receber_0(self):
        self.assertAlmostEqual(converte_F_para_C(0), -17.77, places=1)


class TestConverteCParaF(TestCase):
    def test_deve_retornar__40_quando_receber__40(self):
        self.assertEqual(converte_C_para_F(-40), -40)
