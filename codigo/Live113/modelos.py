from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from data import OpcoesDeStatus


class ModeloDoItem(BaseModel):
    titulo: str
    status: Optional[OpcoesDeStatus]

class ModeloDoItemResposta(ModeloDoItem):
    id: int