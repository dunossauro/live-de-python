def test(arg, dic={}):
    if arg == 'a':
        dic['a'] = 7

    if arg == 'b':
        dic['b'] = 8

    return dic


print(test('a'))
print(test('b'))
