'''
Notas básicas sobre escalas:

  I  II  III IV V   VI VII - Gaus
  Do Re  Mi  Fa Sol La Si  - Escala de Do Maior
  0  1   2   3  4   5  6   - FoxDot

Notas sobre Acordes:
Acorde de Dó: Dó + Mi + Sol == (0, 2, 4)
Acorde de Ré: Ré + Fá + Si == (0, 2, 4)
'''

# Básico sobre os sintetizadores

print(SynthDefs)  # Mostra os sintetizadores disponíveis

s0 >> pluck()  # Toca eternamente Dó

s0 >> pluck(1)  # Toca eternamente Ré

s0 >> pluck([0, 1, 2])  # Toca eternamente Dó, seguido de Ré, seguido de Mi


# Duração e Andamento

# O andamento é de 120 batatidas por minuto

s0 >> pluck(0, dur=1)  # dur é de duração. O padrão é 1

# A duração aqui se refere a metade do andamento.
# O som será executado a cada meio segundo

# Se fizermos a alteração para duração 2, teremos uma nota por segundo
s0 >> pluck(0, dur=2)

# Se fizermos a alteração para duração 4, teremos uma nota a cada 2 segundos
s0 >> pluck(0, dur=4)

# podemos também diminuir a duração. 1/2 por exemplo, diz que será executada 4 vezes por segundo
s0 >> pluck(0, dur=1/2)

s0 >> pluck(0, dur=1/4)  # 8 vezes por segundo


# O tempo também pode ser executado com uma lista

s0 >> pluck(0, dur=[1, 2])

# Nesse caso a primeira nota terá a duração de 1 e a segunda de 2 em loop
# Nota - Duração
# 0      1
# 0      2
# 0      1
# 0      2
# ...

s0 >> pluck([0, 1], dur=[1, 1/2, 1/4])
# Agora nesse caso temos uma sequência de notas e uma sequência de durações
# Nota - Duração
# 0      1
# 1      1/2
# 0      1/4
# 1      1
# 0      1/2
# 1      1/4
# ...

# Juntando tudo em um dó ré mi fá

s0 >> pluck(
    # do ré mi fa fa fa  do re do re re re    do sol fa mi mi mi   do re mi fa fa fa
    [0, 1, 2, 3, 3, 3] + [0, 1, 0, 1, 1, 1] + [0, 4, 3, 2, 2, 2] + [0, 1, 2, 3, 3, 3], # Sequência de notas
    dur=[1, 1, 1, 1, 1/2, 1/2],  # Variações de tempo
)

# O comportamento da lista de todas segue o padrão das listas em python
# Se forem somadas, gerarão uma nova lista
# por exemplo:
# [0] + [1], retulta em [0, 1]
# A seração foi feita para que fique mais simples entender o padrão
# O que resultaria em [0, 1, 2, 3, 3, 3, 0, 1, 0, 1, 1, 1, 0, 4, 3, 2, 2, 2, 0, 1, 2, 3, 3, 3]

# Volume ou Amplitude
s0 >> pluck(amp=1)  # o valor padrão é de 1

s0 >> pluck(amp=2) # 2 é o dobro de volume

s0 >> pluck(amp=1/2) # 1/2 é metade do volume

# Os volumes também podem ser unidos em uma lista

s0 >> pluck(amp=[1/2, 1])

# O que tem como resultado uma nota em 0.5 e uma nota em 1 em loop
# Da mesma forma que a duração
# Nota - Volume
# 0      1/2
# 0      1
# 0      1/2
# 0      1
# ...

# Pan

# Pan é o parâmetro que diz em qual lado o som vai ser executado
# Direita e esquerda, ou no centro, tocando dos dois lados

s0 >> pluck(pan=0) # 0 é o centro

s0 >> pluck(pan=1) # 1 é a direita

s0 >> pluck(pan=-1) # -1 a esquerda

# O som também pode ser transformado em uma lista
# Com isso podemos varias o pan enquanto o sintetizador toca
s0 >> pluck([0, 2, 4, 6, 8, 10], pan=[-1, 0, 1], dur=1/4)  # de fones fica mais divertido.
