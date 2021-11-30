do >> play(
    'v-o[----]',
    dur=1/2
).every(4, 'stutter')

d1 >> play('(* ) [**]')

s0 >> piano(
    [0, 2],
    oct=4,
    dur=8
) + (0, 2)

s1 >> piano(
    var([0, 2], 8)
) + [0, 2, 4, 2]


s2 >> bass(
    var([0, 2], 8),
    dur=1/2
)

s3 >> ambi([0, 2], dur=8) + (0, 2, 4)


s3.stop()

s4 >> pluck(
    var([0, 1 ,2, 4], 8), dur=1/2
)

s5 >> space(
    var([0, 2, 4], 4),
    oct=6,
    dur=1/2,
    pan=[-1, 0, 1, 0]
)

Clock.bpm = 120
