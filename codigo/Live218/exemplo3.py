import sys

def my_trace(frame, event, arg):
    print(
        frame.f_code.co_name,
    )


def func_a(x):
    return x + 2


def func_b(y):
    return func_a(y) - 3

sys.settrace(my_trace)

val = 7

val_2 = func_b(val)

# print(val_2)
