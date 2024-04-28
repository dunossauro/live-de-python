from logging import DEBUG, INFO, FileHandler, StreamHandler, getLogger

logger = getLogger()
logger.setLevel(DEBUG)

shell_handler = StreamHandler()
shell_handler.setLevel(DEBUG)

logger.addHandler(shell_handler)

file_handler = FileHandler('arquivo.log')
file_handler.setLevel(INFO)

logger.addHandler(file_handler)

logger.info('Tudo certo até aqui!')
