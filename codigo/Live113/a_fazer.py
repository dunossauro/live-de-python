from fastapi import APIRouter
from typing import List, Dict, Any, Optional
from modelos import ModeloDoItem, ModeloDoItemResposta
from data import AFazer, OpcoesDeStatus

a_fazer = AFazer()
router = APIRouter()



@router.get("/", response_model=List[ModeloDoItemResposta])
def listar_a_fazer(status: Optional[OpcoesDeStatus] = None):
    """
    View que retorna lista de itens a fazer
    """
    if status is not None:
        return a_fazer.filtrar(status=status)
    return a_fazer.listar()


@router.post("/", response_model=ModeloDoItemResposta, status_code=201)
def inserir_a_fazer(item_a_inserir: ModeloDoItem):
    """
    View que insere item na lista de itens a fazer
    """
    return a_fazer.inserir(item_a_inserir.dict())

@router.get("/{id_do_item}", response_model=ModeloDoItemResposta)
def pegar_item_a_fazer(id_do_item: int):
    """
    View que mostra um item a partir do id dele
    """
    return a_fazer.pegar(id_do_item)
