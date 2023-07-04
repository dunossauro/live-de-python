import trio


async def task_a(event):
    print('Antes do evento acontecer - Tarefa inicial')
    await trio.sleep(10)
    print('Agora pode acontecer!')
    event.set()
    # Diz que o evento começou


async def task_b(event):
    print('Esperando a liberação do evento')
    await event.wait()
    # Só passará dessa linha quando a task_a der event.set
    print('Evento liberado')


async def main():
    async with trio.open_nursery() as nursery:
        event = trio.Event()
        nursery.start_soon(task_a, event)  # Controla o evento
        nursery.start_soon(task_b, event)  # Aguarda o evento
        nursery.start_soon(task_b, event)  # Aguarda o evento


trio.run(main)
