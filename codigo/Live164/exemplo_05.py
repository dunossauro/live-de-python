from pydantic import BaseModel, validator


class Pedidos(BaseModel):
    ids: list[int]

    @validator('ids', pre=True)
    def convert_ids(cls, v):
        if isinstance(v, str):
            return v.split(';')
        return v

    # @validator('ids', each_item=True)
    # def convert_ids(cls, v):
    #     if v < 0:
    #         raise ValueError()
    #     return v
