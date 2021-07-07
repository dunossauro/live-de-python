from app import Coluna, Quadro, Tarefa


def test_não_deve_existir_nenhuma_coluna_no_quadro(quadro):
    quantidade_de_colunas = len(quadro.colunas)
    assert quantidade_de_colunas == 0


def test_quando_inserir_uma_coluna_deve_existir_uma_coluna(
    quadro
):
    quadro.inserir_coluna(Coluna(nome='A fazer'))

    assert len(quadro.colunas) == 1


def test_quando_inserir_a_coluna_fazendo_deve_estar_no_quadro(
    quadro
):
    quadro.inserir_coluna(Coluna(nome='Fazendo'))

    assert quadro.colunas[0].nome == 'Fazendo'


def test_quando_inserir_uma_tarefa_no_quadro_ela_deve_estar_na_primeira_coluna(
    quadro_com_coluna
):
    quadro_com_coluna.inserir_tarefa(
        Tarefa(nome='Dormir')
    )

    assert len(quadro_com_coluna.colunas[0].tarefas) == 1


def test_quando_inserir_duas_tarefa_no_quadro_elas_devem_estar_na_primeira_coluna(
    quadro_com_coluna
):
    quadro_com_coluna.inserir_tarefa(
        Tarefa(nome='Dormir')
    )
    quadro_com_coluna.inserir_tarefa(
        Tarefa(nome='comer')
    )

    assert len(quadro_com_coluna.colunas[0].tarefas) == 2


def test_quando_mover_cartao_ele_deve_ir_para_coluna_seguinte(
    quadro_com_colunas
):
    tarefa = Tarefa('Usar Mascara!')
    quadro_com_colunas.inserir_tarefa(tarefa)

    quadro_com_colunas.mover(tarefa)

    assert tarefa in quadro_com_colunas.colunas[1]


def test_quando_mover_cartao_ele_deve_ser_removida_da_anterior(
    quadro_com_colunas
):
    tarefa = Tarefa('Usar Mascara!')
    quadro_com_colunas.inserir_tarefa(tarefa)

    quadro_com_colunas.mover(tarefa)

    assert tarefa not in quadro_com_colunas.colunas[0]


from pytest import mark


@mark.exemplo
def test_exemplo_para_brincar(factory_boy_test):
    # breakpoint()
    ...


@mark.parametrize(
    'quadro_parametrizado',
    [1],
    indirect=True
)
def test_passando_parametros_para_fixture(quadro_parametrizado):
    ...
