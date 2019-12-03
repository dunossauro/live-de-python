from typing import List, Dict, Any, Optional, Union
from enum import Enum


class OpcoesDeStatus(str, Enum):
    a_fazer = "A Fazer"
    fazendo = "Fazendo"
    feito = "Feito"


Item = Dict[str, Union[int, str, OpcoesDeStatus]]


class AFazer:
    a_fazer: List[Item] = [
        {
            "id": 1,
            "titulo": "Fazer live",
            "decricao": "Fazer live no canal do edu",
            "status": OpcoesDeStatus.a_fazer,
        },
        {
            "id": 2,
            "titulo": "Ligar Streaming",
            "status": OpcoesDeStatus.a_fazer,
        },
        {
            "id": 3,
            "titulo": "Pentear o cabelo (ou raspar)",
            "status": OpcoesDeStatus.a_fazer,
        },
    ]
    id_atual = 3

    def listar(self):
        return self.a_fazer

    def inserir(self, item: Item) -> Item:
        self.id_atual += 1
        item["id"] = self.id_atual
        self.a_fazer.append(item)
        return item

    def pegar(self, item_id: int) -> Item:
        item = filter(lambda x: x["id"] == item_id, self.a_fazer)
        return list(item)[0]

    def filtrar(self, status: OpcoesDeStatus) -> List[Item]:
        return list(filter(lambda x: x["status"] == status, self.a_fazer))