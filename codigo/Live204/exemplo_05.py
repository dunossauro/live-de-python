from numpy import ones
from eliot import log_call, to_file

to_file(open('eliot.log', 'w'))


@log_call
def palavras(split=False):
    with open('br-utf8.txt') as file:
        if split:
            text = file.read().split('\n')
        else:
            text = file.readlines()[:50]
    return text


@log_call
def numpy_array():
    a = ones((100, 100, 100))
    # b = a.tolist()
    return a #, b

# p1 = palavras(True)
p2 = palavras(False)
# na = numpy_array()
