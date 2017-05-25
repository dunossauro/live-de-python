import ipdb

ipdb.set_trace()


def x():
    def f():
        def z():
            def h():
                def j():
                    for x in range(10):
                        return 4
                return j()
            return h()
        return z()
    return f()

if __name__ == '__main__':
    x()
