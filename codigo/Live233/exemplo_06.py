from typer import Typer
from typer.testing import CliRunner


app = Typer()
test_runner = CliRunner()


@app.command()
def olar(nome: str):
    print(f'Olar {nome}')


def test():
    response = test_runner.invoke(app, ['Eduardo'])
    assert response.exit_code == 0
    assert 'Olar Eduardo' in response.stdout


test()
