from logging import basicConfig
from logging import DEBUG, INFO
from logging import FileHandler, StreamHandler
from logging import Formatter, Filter, critical


class MeuFiltro(Filter):
    def filter(self, record):
        if record.msg.lower().startswith('senha'):
            return False
        return True


formater_file_handler = Formatter(
    '%(asctime)s  %(name)s  %(levelname)s: %(message)s'
)
file_handler = FileHandler("meus_logs.txt", "w")
file_handler.setLevel(INFO)
file_handler.setFormatter(formater_file_handler)
file_handler.addFilter(MeuFiltro())

strem_handler = StreamHandler()
strem_handler.addFilter(MeuFiltro())

logger = basicConfig(
    level=DEBUG,
    encoding='utf-8',
    format='%(levelname)s:%(asctime)s:%(message)s',
    handlers=[file_handler, strem_handler]
)

critical('senha 1234')
critical('test filtro')
critical('filtro test')
