from pydantic import BaseModel, validator


class Cadastro(BaseModel):
    email: str  # Já já vamos ver isso
    senha_1: str
    senha_2: str

    @validator('email')
    def email_deve_ter_arroba(cls, v):
        # v é o valor passado no load
        if '@' not in v:
            raise ValueError('Não tem @ no email')
        return v

    # @validator('*')
    # @validator('senha_1', 'senha_2')
    # def senha_tem_mais_de_10_chars(cls, v):
    #     if len(v) < 10:
    #         raise ValueError('Menor que +10')
    #     return v

    @validator('senha_2')
    def senha_iguais(cls, v, values):
        if v == values['senha_1']:
            return v
        raise ValueError('Senhas diferenets')
