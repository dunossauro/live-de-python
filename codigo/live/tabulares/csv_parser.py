with open('episodios.csv') as csv_file:
    samurai = csv_file.readlines()

parserd_samurai = list(map(lambda x: x.strip().split(';'), samurai))
