from faststream import FastStream
from faststream.redis import RedisBroker


broker = RedisBroker()
app = FastStream(broker)


@broker.subscriber('test')
async def handler(message):
    print(message)
    return message


import pytest

@pytest.mark.asyncio
async def test_handler():
    assert await handler('teste') == 'teste'


from faststream.redis import TestRedisBroker

@pytest.mark.asyncio
async def test_handler_integration():
    async with TestRedisBroker(broker) as br:
        response = await br.request(
            'teste', channel='test'
        )
        assert response.body.decode() == 'teste'
