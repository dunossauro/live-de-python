from setuptools import setup

requirements = ['click']

setup(
    name='Live 88',
    version='1',
    packages=['app'],
    entry_points={
        'console_scripts':
            ['live88 = app:cli']
    }
)
