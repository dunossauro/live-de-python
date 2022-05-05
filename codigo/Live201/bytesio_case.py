from io import BytesIO
from tempfile import SpooledTemporaryFile
from memory_profiler import profile


@profile
def test_tempfile():
    with open('image_test.jpg', 'rb') as file:
        um_mb = 1_000_000
        with SpooledTemporaryFile(max_size=um_mb) as stf:
            em_memoria = stf.write(file.read())
            print(stf.name)
            return em_memoria

@profile
def test_bytesio():
    with open('image_test.jpg', 'rb') as file:
        em_memoria = BytesIO(file.read())
        return em_memoria

test_tempfile()
test_bytesio()
