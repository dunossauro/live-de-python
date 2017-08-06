from threading import Timer
from time import sleep
var = True


def hello():
    global var
    print('hello timer')
    var = False


t = Timer(2, hello)
t.start()

t2 = Timer(1, hello)
t2.start()

while var:
    print('hello')
    sleep(0.3)
