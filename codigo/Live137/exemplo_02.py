from pendulum import now

print(now().add(days=5).in_tz('Europe/Paris'))
