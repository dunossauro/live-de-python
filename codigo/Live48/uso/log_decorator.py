from functools import wraps
import logging

log_format = '%(asctime)s:%(filename)s:%(levelname)s:%(message)s'

logging.basicConfig(level=logging.DEBUG,
                    format=log_format)

logger = logging.getLogger(__name__)


def log(func):
    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        l_string = f'func:{func}:args:{args}:kwargs:{kwargs}:result:{result}'
        logger.debug(l_string)
        return result
    return inner


@log
def xpto(a, **kwargs):
    return a, kwargs
