from logging.handlers import RotatingFileHandler
from loguru import logger

logger.add(RotatingFileHandler('file'), level='DEBUG',
           serialize=True)

logger.info('Passei aqui!')
