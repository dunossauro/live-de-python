digitos = [0, 1, 2, 3]

strings = ['zero', 'um', 'dois', 'três']

numeros = {digito:string for digito, string in zip(digitos, strings)}
# {0: 'zero', 1: 'um', 2: 'dois', 3: 'três'}

dict((digito, string) for digito, string in zip(digitos, strings))
# {0: 'zero', 1: 'um', 2: 'dois', 3: 'três'}
