import trio
import pytest


async def sleep_mucho():
    await trio.sleep(5)
    return 'Batatinha!'


@pytest.mark.trio  # Roda essa função de teste no trio.run()
async def test_sleep_mucho(autojump_clock):
    resultado = await sleep_mucho()
    assert resultado == 'Batatinha!'
