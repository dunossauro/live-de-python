from faststream import FastStream
from faststream.redis import RedisBroker

broker = RedisBroker('redis://localhost:6379')
app = FastStream(broker)

from pydantic import BaseModel


class Event(BaseModel):
    id: int | None = None
    message: str

from fast_depends import Depends

async def get_session():
    yield ...

@broker.subscriber('test')
async def handler(modelo_do_evento: Event, session = Depends(get_session)):
    ...
    return modelo_do_evento
