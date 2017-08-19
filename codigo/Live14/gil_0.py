from time import time

numbers = [2139079, 1214759, 1516637, 1852285]


def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


start = time()
for number in numbers:
    list(factorize(number))
end = time()

print(f'{end-start}')  # ~ 0.4634
