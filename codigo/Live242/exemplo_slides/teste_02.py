import trio
import pytest

async def meromy_recever(recever):
    async with recever:
        async for value in recever:
            print(f'recever: {value}')


@pytest.mark.trio
async def test_memory(capsys, nursery):
    sender, recever = trio.open_memory_channel(0)
    nursery.start_soon(meromy_recever, recever)
    await sender.send('Mensagem')
    sender.close()

    out, err = capsys.readouterr()
    assert out == 'recever: Mensagem\n'
