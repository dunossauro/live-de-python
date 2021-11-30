Root.default = 'C'
Scale.scale = 'major'
Clock.bpm = 120

notas = [0, 3, 5, 4]
frequencia = var(notas, 4)

d0 >> play(
    '<x |o2| ><---{[----]-*}>',
    sample=4,
    dur=1/2
)


s0 >> space(
    notas,
    dur=1/4,
    apm=3,
    pan=[-1, 0, 1]
)

s1 >> bass(
    frequencia,
    dur=1/4,
    oct=4,
)

s2 >> spark(
    frequencia,
    dur=[1/2, 1/4],
) + (0, 2, 4)


s3 >> pluck(
    s2.degree,
    dur=[1/4, 1, 1/2, 2],
    pan=[-1, 1]
)

