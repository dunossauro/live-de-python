class LiveError(Exception):
    def __init__(self, msg):
        self.m = msg

    def __str__(self):
        return self.m

    @staticmethod
    def batatinhas():
        return 'batatinhas'


try:
    print('dentro do try')
    raise LiveError('olá erro da live')
except LiveError as l:
    print('dentro do except')
    print(l.batatinhas())
