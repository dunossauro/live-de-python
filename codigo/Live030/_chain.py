def chain(*iters):
    for l in iters:
        yield from l
