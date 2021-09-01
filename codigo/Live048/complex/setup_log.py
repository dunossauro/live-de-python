import logging
import logging.config

logging.config.fileConfig(fname='simple_logger.ini')

logger = logging.getLogger('root')

logger.info('oi bb')
