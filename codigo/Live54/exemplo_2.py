from concurrent.futures import ProcessPoolExecutor, as_completed

l_ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def ident(x):
    return x


with ProcessPoolExecutor() as exe:
    """
    GIL: tarefaz bloqueantes de I/O.
    
    Vão dar bypass no GIL
    """
    l_futures = []
    for e in l_ints:
        worker = exe.submit(ident, e)
        l_futures.append(worker)

    # result_0.add_done_callback(partial(print, 'acabei'))
    for worker in as_completed(l_futures):
        resp = worker.result()
        print(worker, resp)
