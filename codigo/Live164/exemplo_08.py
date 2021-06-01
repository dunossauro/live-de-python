from pydantic import BaseSettings, BaseModel
from typing import Literal, Union


class TestConfig(BaseSettings):
    env: Literal['test']
    xpto: str = 'MEU AMBIENTE DE TESTES'


class ProdConfig(BaseSettings):
    env: Literal['prod']
    gatinho: str = 'MEU AMBIENTE DE GATINHO'


class DevConfig(BaseSettings):
    env: Literal['dev']
    cachorrinho: str = 'MEU AMBIENTE DE CACHORRO'


class Config(BaseModel):
    config: Union[DevConfig, TestConfig, ProdConfig]
