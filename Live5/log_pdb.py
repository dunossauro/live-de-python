from logging import getLogger, basicConfig, DEBUG
from sys import exc_info
from collections import deque
from pdb import post_mortem

basicConfig(filename='test.log',
            filemode='w',
            level=DEBUG)

log = getLogger(__name__)


log.info('teste2')
log.info('teste3')
log.info('teste4')
log.info('teste1000')

def debug(debug=False):
    def tail_log(func):
        def exectute_func(*args):
            try:
                func(*args)
            except Exception as error:
                log.info('{} args:{} error:{}'.format(func.__name__,
                                                      args,
                                                      error))
                if debug:
                    for line in deque(open('test.log'), 10):
                        print(line)
                    post_mortem(exc_info()[2])
        return exectute_func
    return tail_log


@debug(True)
def div(x, y):
    log.info('Entrei na função {}'.format(div.__name__))
    return x / y


div(2, 0)
