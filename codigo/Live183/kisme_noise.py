so >> play('<{kissme}><{-=V}><{noise}>')

su >> play('<{kissme}><{noise}><{-=V}>')

s0 >> noise(
    PRand(0, 7), oct=4, dur=8, amp=.7
)

s1 >> space(
    PRand(0, 7), oct=5, dur=2
)

s2 >> space(
    s0.degree + PRand(0, 7)
)

s3 >> karp(
    s0.degree, oct=1, amp=4, dur=1/2
) + [0, 2, 4]


s4 >> sawbass(
    s1.degree, oct=2, amp=3
)
