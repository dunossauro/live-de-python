import asyncio

# @asyncio.coroutine
async def empacotar_bala():
    # print 1
    print('empacotando balas')

    # para para ver se tem clientes
    # yield from asyncio.sleep(0.1)
    await asyncio.sleep(0.1)

    # print 3
    print('Verifiquei, não tem ninguém... vou empacotar balas')

# @asyncio.coroutine
async def atender_balcao():
    # print 2
    print('Verificando se há clientes')

    # yield from asyncio.sleep(0.1)
    await asyncio.sleep(0.1)

    # print 4
    print('Não, não há clientes')

# definindo um loop
loop = asyncio.get_event_loop()

tasks = [loop.create_task(empacotar_bala()),
         loop.create_task(atender_balcao())]

wait_tasks = asyncio.wait(tasks)

loop.run_until_complete(wait_tasks)

loop.close()
