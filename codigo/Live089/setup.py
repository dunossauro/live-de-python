"""
LASH setup.

Instalar o lash na nossa máquina
"""
from setuptools import setup

setup(
    name='lash',
    version='0.0.1',
    packages=['lash'],
    entry_points={
        'console_scripts':
            ['lash  = lash:cli']
    }
)
