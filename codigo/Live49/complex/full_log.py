import logging

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Console Handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

# File Handler
fh = logging.FileHandler('log.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# Adicionando o handlers
logger.addHandler(ch)
logger.addHandler(fh)

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
