from asyncio import sleep
from faststream import FastStream, Logger
from faststream.redis import RedisBroker
from tenacity import retry, stop_after_attempt, wait_random_exponential

broker = RedisBroker()
app = FastStream(broker)


def on_final_failure(retry_state):
    print('Cagou tudo!')
    print(retry_state.kwargs)
    breakpoint()


@broker.subscriber('topico_a')
@broker.publisher('topico_b')
@broker.publisher('topico_c')
@retry(
    stop=stop_after_attempt(5),
    wait=wait_random_exponential(multiplier=1, max=60),
    retry_error_callback=on_final_failure,    
)
async def handler_a(message, logger: Logger):
    await sleep(2)

    import random
    if random.choice([True, False]):
        logger.warning('Deu ruim!')
        raise Exception()

    return message


@broker.subscriber('topico_b')
async def handler_b(message, logger: Logger):
    logger.warning('topico_b')
    await sleep(2)
    return message

@broker.subscriber('topico_c')
@broker.publisher('topico_a')
async def handler_c(message, logger: Logger):
    logger.warning('topico_c')
    await sleep(2)
    return message
