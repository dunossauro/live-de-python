import logging
# pip install python-json-logger
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

shell_handler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
shell_handler.setFormatter(formatter)
logger.addHandler(shell_handler)

logger.info('Passei aqui!')
