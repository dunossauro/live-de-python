from sys import stderr
from loguru import logger

logger.remove()

logger.add(
    sink=stderr,
    format='{time} <r>{level}</r> <g>{message}</g> {file}',
    filter=lambda rec: 'senha' not in rec['message'].lower(),
    level='INFO',
)

logger.critical('senha')
logger.debug('Debug')
logger.info('Info')
logger.warning('Warning')
