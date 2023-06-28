from itertools import cycle
atendimento = cycle(['Monica', 'Pedro', 'Ana', 'Sergio'])
pacientes = range(10)


for paciente in pacientes:
    print(f'{paciente=} - Atendimento {next(atendimento)}')
