from app import converte


def test_converte_deve_retornar_0_quando_receber_32():
    assert converte(32) == 0

def teste_converte_deve_retornar__40_quando_receber__40():
    assert converte(-40) == -40
