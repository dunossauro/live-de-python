from collections import OrderedDict

# OrderDict lembra as ordens em que os valores forão inseridos
d = OrderedDict()
d[0] = 'Linus'
d[999] = 'Live de Python'
d # OrderedDict([(0, 'Linus'), (999, 'Live de Python')])

d.update({3: 'jogo da velhar'})
d # OrderedDict([(0, 'Linus'), (999, 'Live de Python'), (3, 'jogo da velhar')])
