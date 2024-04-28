from logging import WARNING, getLogger, StreamHandler, FileHandler

logger = getLogger()
logger.setLevel(WARNING)
logger.addHandler(StreamHandler())
logger.addHandler(FileHandler('arquivo.log'))

logger.info('Passei aqui!')
logger.critical('DEU RUIM!')


from logging import Handler


class CustomHandler(Handler):
    def emit(self, record: LogRecord) -> None:
        return super().emit(record)
