from pydantic import BaseSettings, Field, PostgresDsn


# class MinhaConfig1(BaseSettings):
#     mongo_url: str = Field(..., env='mongo_url')
#     postgres_url: str = Field(..., env='postgres_url')


# print(MinhaConfig1())


class TestConfig(BaseSettings):
    postgres_url: PostgresDsn

    class Config:
        env_prefix = 'test_'


print(TestConfig())
