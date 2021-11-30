Clock.bpm = 120

d1 >> play('X-|o2|{-[----]*}', sample=4, dur=1/2)

print(SynthDefs)

s1 >> spark(
    var([0, 2, 4], 4), dur=[1/2, 1/4]
) + (0, 2, 4)


s2 >> bass(
    var([0, 2, 4], 4), dur=[1/4]
)

s3 >> space(
   PRand(0, 7), dur=2
)
