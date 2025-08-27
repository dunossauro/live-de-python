import json
from asyncio import sleep
from datetime import datetime
from enum import Enum

from fast_depends import Depends, inject
from faststream import FastStream, Logger
from faststream.redis import RedisBroker
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import Mapped, mapped_column, registry
from taskiq.schedule_sources import LabelScheduleSource
from taskiq_faststream import BrokerWrapper, StreamScheduler
from tenacity import retry, stop_after_attempt, wait_random_exponential


class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str


# sqlalchemy
engine = create_async_engine(Settings().DATABASE_URL)
table_registry = registry()

# faststream
broker = RedisBroker(Settings().REDIS_URL)
app = FastStream(broker)
# Taskiq
taskiq_broker = BrokerWrapper(broker)


taskiq_broker.task(
    channel='periodic',
    message='',
    schedule=[{'cron': '*/5 * * * *'}],  # A cada 5 minutos
)

scheduler = StreamScheduler(
    broker=taskiq_broker,
    sources=[LabelScheduleSource(taskiq_broker)],
)


class Produto(BaseModel):
    p_id: int
    c_id: int


class _Status(str, Enum):
    checkout = 'checkout'
    estoque = 'estoque'
    pagamento = 'pagamento'
    envio = 'envio'
    nota = 'nota'
    erro = 'erro'


@table_registry.mapped_as_dataclass
class Status:
    __tablename__ = 'status'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)

    c_id: Mapped[int]
    status: Mapped[_Status]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )


async def get_session():
    async with AsyncSession(engine, expire_on_commit=False) as s:
        yield s


@inject
async def gravar_status(
    c_id: int, status: _Status, session: AsyncSession = Depends(get_session)
):
    s = Status(c_id=c_id, status=status)

    try:
        session.add(s)
        await session.commit()
        print(f'[{status}] Status registrado para compra {c_id}')
    except Exception as e:
        await session.rollback()
        raise e

    return s


async def on_final_failure(retry_state):
    print('on_final_failure')
    try:
        del retry_state.kwargs['logger']
    finally:
        # await broker.publish(
        #     channel='DLQ',
        #     message={retry_state.fn.__name__: retry_state.kwargs},
        # )

        redis = broker._connection

        data = retry_state.kwargs.copy()
        for k, v in data.items():
            if hasattr(v, 'dict'):
                data[k] = v.dict()

        message = json.dumps({retry_state.fn.__name__: data})

        await redis.lpush('DLQ', message)

        await gravar_status(
            c_id=retry_state.kwargs.get('c_id'), status=_Status.erro
        )


@broker.subscriber('checkout')
@broker.publisher('estoque')
@retry(
    stop=stop_after_attempt(5),
    retry_error_callback=on_final_failure,
    wait=wait_random_exponential(multiplier=1, max=60),
)
async def checkout(produto: Produto, logger: Logger) -> int:
    logger.info('Iniciando checkout')
    await sleep(2)

    import random

    choice = random.choice([True, False, False, False])
    if choice:
        logger.info(f'Erro no checkout, tentando novamente... {choice=}')
        raise Exception('Erro forçado!')

    status = await gravar_status(produto.c_id, _Status.checkout)

    logger.info('Até o fim!!!')
    return status.c_id


@broker.subscriber('estoque')
@broker.publisher('pagamento')
async def estoque(id_compra: int):
    """Implementar lógica de estoque..."""
    await sleep(10)

    await gravar_status(id_compra, _Status.estoque)

    return id_compra


@broker.subscriber('pagamento')
@broker.publisher('envio')
@broker.publisher('nota_fiscal')
async def pagamento(id_compra: int):
    """Implementar lógica de pagamento..."""
    await sleep(10)

    await gravar_status(id_compra, _Status.pagamento)

    return id_compra


@broker.subscriber('envio')
async def envio(id_compra: int):
    """Implementar lógica de envio..."""
    await sleep(10)

    await gravar_status(id_compra, _Status.envio)

    return id_compra


@broker.subscriber('nota_fiscal')
async def nota_fiscal(id_compra: int, logger: Logger):
    """Implementar lógica de nota fiscal..."""
    await sleep(5)
    await gravar_status(id_compra, _Status.nota)
    logger.info(f'Nota fiscal gerada para compra {id_compra}')
    return id_compra


@broker.subscriber('periodic')
async def reprocessar_dlq(msg: str, logger: Logger):
    """Evento periódico que tenta reprocessar as mensagens que deram errado."""
    logger.info(f'Reprocessando mensagem da DLQ: {msg}')
    redis = broker._connection

    while True:
        raw = await redis.rpop('DLQ')
        if not raw:
            break

        try:
            data = json.loads(raw)
            handler = list(data.keys())[0]
            kwargs = data[handler]

            logger.warning(f'Reprocessando mensagem para {handler}: {kwargs}')
            await broker.publish(channel=handler, message=kwargs)
        except Exception as e:
            logger.error(f'Erro ao reprocessar: {e}')
