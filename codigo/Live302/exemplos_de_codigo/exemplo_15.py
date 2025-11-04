import io, os
from contextlib import chdir, contextmanager, redirect_stdout, suppress

target = io.StringIO()

@contextmanager
def temp_context():
    print("Entrou")
    print(os.getcwd())
    try:
        yield
    finally:
        print("Saiu")
        # Nunca vai sair no exemplo por conta do erro.

with (
    suppress(FileNotFoundError),
    chdir("/tmp"),
    redirect_stdout(target),
    temp_context(),
):
    print("Diretório temporário ativo!")
    print(os.getcwd())
    open("inexistente.txt")


print(target.getvalue())
