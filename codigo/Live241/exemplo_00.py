def count(start, step=1):
    count = start
    while True:
        yield count
        count += step


counter = count(1)

print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3

for val in counter:
    print(val)
