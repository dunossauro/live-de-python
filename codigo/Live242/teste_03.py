import trio
import pytest


async def consumer(receive_channel):
    async with receive_channel:
        async for value in receive_channel:
            print(f'got value {value}')


@pytest.mark.trio
async def test_com_nursery(capsys, nursery):
    sender, recever = trio.open_memory_channel(0)

    nursery.start_soon(consumer, recever)

    await sender.send(1)
    await trio.sleep(0)
    sender.close()

    message, _ = capsys.readouterr()

    assert message == 'got value 1\n'
