from trio import run


async def main():
    print('Olá Trio!')
    return ['']


run(main)
