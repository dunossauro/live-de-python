from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = cythonize(
    [Extension(
        'c_fib_import',
        sources=['c_fib.c', 'c_fib_import.pyx']
    )]
)

setup(
    ext_modules=exts
)
