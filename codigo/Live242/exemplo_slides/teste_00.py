import trio
import pytest

async def sleep_test():
    await trio.sleep(5_000)
    return 'PEI!'

@pytest.mark.trio
async def test_sleep_test(autojump_clock):
    """Teste sleep_test()."""
    result = await sleep_test()
    assert result == 'PEI!'

@pytest.mark.trio
async def test_clock(autojump_clock):
    """O mecanismo de jump."""
    from trio import current_time

    await trio.sleep(20000)
    assert 20000 == current_time()
