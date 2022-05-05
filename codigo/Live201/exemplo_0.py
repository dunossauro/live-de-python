from tempfile import TemporaryFile


with TemporaryFile(mode='w+') as temp_file:
    print(temp_file.name)
    temp_file.write('batatinhas')
    temp_file.seek(0)
    print(temp_file.read())
