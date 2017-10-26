with open('episodios.csv') as csv_file:
    samurai = csv_file.readlines()

parsed_samurai = list(map(lambda x: x.strip().split(';'), samurai))
