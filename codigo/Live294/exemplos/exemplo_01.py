from faststream import FastStream
from faststream.redis import RedisBroker

broker = RedisBroker('redis://localhost:6379')
app = FastStream(broker)

from pydantic import BaseModel


class Event(BaseModel):
    id: int | None = None
    message: str


@broker.subscriber('topico_a')
async def handler_a(modelo_do_evento: Event):
    await broker.publish(modelo_do_evento, 'topico_b')

@broker.subscriber('topico_b')
async def handler_b(modelo_do_evento: Event):
    return modelo_do_evento
