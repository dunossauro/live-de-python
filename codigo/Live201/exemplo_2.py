from tempfile import NamedTemporaryFile


with NamedTemporaryFile(
    suffix='.mp3',
    prefix='ldp_',
    delete=False
) as file:
    print(file.name)
    input('Esperando o bb olhar!')
