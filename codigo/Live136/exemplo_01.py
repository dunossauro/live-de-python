from pendulum import now, timezone

#IANA
#pytz

n = now('UTC')

tz1 = timezone('America/Toronto')
tz2 = timezone('America/Sao_Paulo')

print(n)
print(tz1.convert(n))
print(n.in_tz('America/Sao_Paulo'))
