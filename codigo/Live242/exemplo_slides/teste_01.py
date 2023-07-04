import trio
import pytest

async def fetch():
    with trio.fail_after(10):
        await trio.sleep(11)
        # ...

        return 'xpto'

@pytest.mark.trio
async def test_fetch(autojump_clock):
    with pytest.raises(trio.TooSlowError):
        await fetch()
