def subtracao(x, y):
    from time import sleep
    sleep(1)
    return x - y


def soma(x, y):
    return x + y


def conta(x, y, z):
    return subtracao(soma(soma(x, y), z), z)


# import cProfile
# import pstats

# prof = cProfile.Profile()

# prof.enable()

# Inicio do miolo
conta(1, 2, 3)
# Fim do miolo

# prof.disable()

# stats = pstats.Stats(prof).sort_stats('ncalls')
# stats.print_stats()
