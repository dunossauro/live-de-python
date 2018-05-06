"""
Exemplo 2.

Como escrever o log em um arquivo
"""
import logging

logging.basicConfig(filename='exemplo_2.log', level=logging.DEBUG)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
