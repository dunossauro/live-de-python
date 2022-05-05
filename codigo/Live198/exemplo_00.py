from logging import basicConfig         # configuração
from logging import DEBUG               # Level
from logging import debug, info, error  # Cahamadas
from logging import FileHandler, StreamHandler  # Handlers


basicConfig(
    level=DEBUG,
    encoding='utf-8',
    format='%(levelname)s:%(asctime)s:%(message)s',
    handlers=[FileHandler("meus_logs.txt", "w"), StreamHandler()]
)

debug('Mensagem de debug')
info('Mensagem informativa')
error('Mensagem de erro')
