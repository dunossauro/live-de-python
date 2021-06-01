from pydantic import BaseModel, EmailStr, Field
from decimal import Decimal
from datetime import datetime


class Cadastro(BaseModel):
    # email: EmailStr
    valor_do_pedido: Decimal = Field(Decimal(1.0), gt=1.0)
    criado_em: datetime = Field(default_factory=datetime.now)
    atualizado_em: datetime
