"""
Instalação

$ pip install faststream[redis,cli] PyYAML

Subir a imagem:

$ podman run -p 6379:6379 docker.io/redis

Rodar o faststream via CLI:

$ faststream run serve exemplos.exemplo_00:app

AsyncAPI:

Gerar o yaml:

$ faststream docs gen --yaml exemplos.exemplo_00:app

Converter pra doc:

$ npx @asyncapi/cli generate fromTemplate asyncapi.yaml @asyncapi/html-template@3.0.0 --use-new-generator -o docs --force-write
"""
import logging
from faststream import FastStream
from faststream.redis import RedisBroker

logger = logging.getLogger(__name__)
broker = RedisBroker('redis://localhost:6379')

app = FastStream(broker)


@broker.subscriber('test')
async def soma(a: int, b: int):
    logger.info(f'soma: result: {a + b}')
    return a + b


# --------------
# import pytest

# @pytest.mark.asyncio
# async def test_soma():
#     assert await soma(1, 2) == 3


# # Integração
# from faststream.redis import TestRedisBroker

# @pytest.mark.asyncio
# async def test_handler():
#     # assert await soma(1, 2) == 3
#     async with TestRedisBroker(broker) as br:
#         response = await br.request({'a': 1, 'b': 2}, channel='test')
#         assert response.body.decode() == '3'
