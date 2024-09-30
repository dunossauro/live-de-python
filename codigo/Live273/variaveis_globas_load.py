# Caso da demora
# Conexão com o banco, busca por variáveis, ...

from __future__ import annotations
from time import sleep


class Database:
    instance: Database

    @classmethod
    def get_instance(cls) -> Database:
        if not hasattr(cls, 'instance'):
            cls.instance = Database()
        return cls.instance

    def __init__(self):
        self.conn = self._get_conn()

    def _get_conn(self):
        sleep(3)
        return 'Cn'


# ---

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    @classmethod
    def get_instance(cls) -> Settings:
        if not hasattr(cls, 'instance'):
            cls.instance = Settings()
        return cls.instance

    model_config = SettingsConfigDict(env_file='.env')

    API_KEY: str
