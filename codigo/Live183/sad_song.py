notes = P[0, 2, 4]
seq = var(notes, 4)
Scale.default = 'minor'

d0 >> play(
    '^:|@3|:',
)

s0 >> dbass(
    seq,
    amp=.7,
    dur=PDur(3, 8),
    hpf=linvar([300, 0, 400, 600], 4),
    pan=linvar([-1, 0, 1, 0], 16)
)

s1 >> space(
    seq + [7, 0, -7, -14],
    oct=4,
    hpf=linvar([500, 1000, 300, 2000], 4),
    dur=2,
    amp=2
)

s2 >> bell(
    seq,
    oct=3,
    amp=0.6,
    pan=linvar(P[-1, 0, 1, 0].reverse(), 16)
)

s3 >> jbass(
    seq, oct=4, dur=2
)

s4 >> ambi(
    seq
) + (0, 2, 4)
