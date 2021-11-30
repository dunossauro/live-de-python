"""
Notas = E, A7+
"""
Clock.bpm = 107

s0 >> play(
    'x-:-', dur=1/2, amp=5
)

s1 >> bass(
    [2,5], dur=4
)

print([x for x in SynthDefs if 'bass' in x])



