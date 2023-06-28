# fake pandas describe
import statistics
from itertools import tee

data_stream = map(float, open("data.txt"))
data1, data2, data3 = tee(data_stream, 3)

average = statistics.mean(data1)
median = statistics.median(data2)
percentile_50 = statistics.median_grouped(data3)

print(
    f'Average: {average}, Median: {median}, 50%: {percentile_50}'
)
