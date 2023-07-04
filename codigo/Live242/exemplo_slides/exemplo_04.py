from trio import run, open_nursery
from trio.abc import Instrument
import trio
from httpx import AsyncClient, ConnectTimeout


async def fetch(url):
    async with AsyncClient() as client:
        response = await client.get(url, timeout=None)
        data = response.json()
        print(data['id'], data['name'])


async def main():
    url = 'https://pokeapi.co/api/v2/pokemon/{}'
    try:
        async with open_nursery() as nursery:
            for n in range(1, 2):
                poke_url = url.format(n)
                print(f'Iniciando: {poke_url}')
                nursery.start_soon(fetch, poke_url)

    except *ConnectTimeout as ex:
        print(ex)
        for error in ex.exceptions:
            print(f'ERROR: {error.request.url}')


class Tracer(Instrument):
    def before_run(self):
        print("!!! run started")

    def _print_with_task(self, msg, task):
        # repr(task) is perhaps more useful than task.name in general,
        # but in context of a tutorial the extra noise is unhelpful.
        print(f"{msg}: {task.name}")

    def task_spawned(self, task):
        self._print_with_task("### new task spawned", task)

    def task_scheduled(self, task):
        self._print_with_task("### task scheduled", task)

    def before_task_step(self, task):
        self._print_with_task(">>> about to run one step of task", task)

    def after_task_step(self, task):
        self._print_with_task("<<< task step finished", task)

    def task_exited(self, task):
        self._print_with_task("### task exited", task)

    def before_io_wait(self, timeout):
        if timeout:
            print(f"### waiting for I/O for up to {timeout} seconds")
        else:
            print("### doing a quick check for I/O")
        self._sleep_time = trio.current_time()

    def after_io_wait(self, timeout):
        duration = trio.current_time() - self._sleep_time
        print(f"### finished I/O check (took {duration} seconds)")

    def after_run(self):
        print("!!! run finished")


run(main, instruments=[Tracer()])
