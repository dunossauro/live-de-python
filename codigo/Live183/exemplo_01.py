'''
Sintetizadores

Tres partes:
    1 - Samples 
      1.1 - loop
      1.2 - strech
      1.3 - play
'''

# Tocar audio externo

l0 >> loop(
    '/home/dunossauro/git/fox_music/ldp.wav',
    dur=[1/2, 1/4, 1/4, 1/4, 2],
)

s0 >> stretch(
    '/home/dunossauro/git/fox_music/ldp.wav',
    dur=6,
).stop()

mo >> play('x-o[----]')
