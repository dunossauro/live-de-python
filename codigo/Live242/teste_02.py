import trio
import pytest


async def mooveee():
    with trio.fail_after(10):
        await trio.sleep(11)

        # ... Código bacana!

        return 'SHOW D BOLA!'

@pytest.mark.trio  # Roda essa função de teste no trio.run()
async def test_mooveee(autojump_clock):
    with pytest.raises(trio.TooSlowError):
        await mooveee()
