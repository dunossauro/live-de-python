import tempfile

tempfile.tempdir = '.cache'

print(tempfile.gettempdir())

with tempfile.NamedTemporaryFile() as tmp_file:
    tmp_file.write(b'batatinha')
    input('Aguardando aviões!')
