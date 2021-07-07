from dataclasses import dataclass


@dataclass
class Tarefa:
    nome: str


class Coluna:
    def __init__(self, nome, tarefas=None):
        self.nome = nome
        self.tarefas = tarefas or []

    def __getitem__(self, item):
        return self.tarefas[item]

    def insere_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def remover_tarefas(self, tarefa):
        self.tarefas.remove(tarefa)

    def __repr__(self):
        return f'Coluna(nome="{self.nome}", tarefas={self.tarefas})'


class Quadro:
    def __init__(self, colunas=None):
        self.colunas = colunas or []

    def inserir_coluna(self, coluna):
        self.colunas.append(coluna)

    def inserir_tarefa(self, tarefa):
        self.colunas[0].insere_tarefa(tarefa)

    def __repr__(self):
        return f'Quadro(colunas={self.colunas})'

    def mover(self, tarefa):
        if tarefa in self.colunas[0]:
            self.colunas[0].remover_tarefas(tarefa)
            self.colunas[1].insere_tarefa(tarefa)
