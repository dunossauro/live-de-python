from csv import reader
from matplotlib import pyplot as plt

with open('temperaturas.csv') as file:
    parsed = reader(file)

    data_1999 = filter(lambda v: v[0] == '1999.0', parsed)

    max_temp = [float(v[3]) for v in data_1999 if v[3]]
    min_temp = [float(v[4]) for v in data_1999 if v[4]]
    med_temp = [float(v[5]) for v in data_1999 if v[5]]

    # import pdb; pdb.set_trace()

    plt.plot(max_temp, label='MAX')
    plt.plot(min_temp, label='MIN')
    plt.plot(med_temp, label='MED')
