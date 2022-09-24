def b(): assert False
def a(): return b()
def xpto(): return a()


xpto()
