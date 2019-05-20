from .path import paths
from .pipes import pipes
from .progress import pb, check_url
from click import group


@group('cli')
def cli():
    ...

cli.add_command(paths)
cli.add_command(pipes)
cli.add_command(pb)
cli.add_command(check_url)

cli()
