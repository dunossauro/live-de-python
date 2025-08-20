import pendulum

dt_meu = pendulum.now(tz='America/Sao_Paulo')
dt_will = dt_meu.in_timezone('Europe/Berlin')
print(dt_meu, '\n', dt_will)
# 2025-08-10 22:27:38.766820-03:00
# 2025-08-11 03:27:38.766820+02:00
