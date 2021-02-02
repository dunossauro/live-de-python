from corrotina import corrotina
from collections import namedtuple

log_line = namedtuple('Log', 'data ampm bool nome telefone email')


@corrotina
def re_type():
    types = [str, str, eval, str, str, str]
    value = None
    while True:
        unformated = yield value
        value = [f(d) for f, d in zip(types, unformated)]


@corrotina
def convert_to_tuple():
    data = None
    while True:
        value = yield data
        data = log_line(*retype.send(value.split(',')))


@corrotina
def grep(pattern, target):
    for line in target:
        if pattern in line:
            yield tr.send(line)


@corrotina
def filter_bool(target):
    for log in target:
        if log.bool:
            yield log


logs = open('logs.csv')

tr = convert_to_tuple()
retype = re_type()

a = grep('AM', logs)
b = filter_bool(a)
