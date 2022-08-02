def contador(start=0):
    count = start

    def interna():
        nonlocal count
        count += 1
        return count

    return interna


c = contador()

print(c())  # 1
print(c())  # 2
print(c())  # 3
print(c())  # 4
