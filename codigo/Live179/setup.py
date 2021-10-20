from setuptools import setup

setup(
    name='meu_pacote',
    version='0.0.1',
    packages=['meu_pacote'],
    install_requires=['httpx'],
    entry_points={
        'console_scripts': ['meu-cli = meu_pacote.minha_lib:cli']
    }
)
