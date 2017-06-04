from pdb import set_trace
var = 7

def func():
    global var
    print(var)
    var = 18
    print(var)
    # set_trace()


func()
print(var)
