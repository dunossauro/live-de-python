def formatação(quem, prog, n):
    return '{quem} está apresentando a {prog} #{n}'


nome = 'Eduardo'
programa = 'Live de Python'
numero = 197


breakpoint()

formatado = formatação(nome, programa, numero)

breakpoint()

# TESTE!
assert formatado == 'Eduardo está apresentando a Live de Python #197'
