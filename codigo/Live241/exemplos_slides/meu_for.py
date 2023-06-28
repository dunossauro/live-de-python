a = [1, 2, 3]
  
it = iter(a)  # chama __iter__
  
while True:
    try:
        x = next(it)  # chama __next__
    except StopIteration:
        break
    print(x)
