# Escopo de variáveis

## Sobre nomes e objetos

Uma variável é, na verdade, um **nome** que aponta para um **objeto**. Isso quer dizer que `a = 1` cria um **Nome** `a` que aponta para o **objeto** `1`, que é um objeto do tipo `int`. Se após isso eu fizer `b = 1`, crio um novo **nome**, que aponta para *o mesmo objeto inteiro* `1`, e não um novo objeto, em um novo endereço de memória. Isso deve ser sempre levado em consideração no Python.

## Sobre Namespaces e Escopos

Um **namespace** é um mapeamento de **nomes**. Ele simplesmente se lembra para quais objetos um nome aponta.

O namespace principal do Python, que é criado quando chamamos o interpretador, é o `__main__`. Sempre que eu executo um arquivo ou abro o interpretador, esse é o namespace que ele abre e todos os nomes que eu criar são salvos nesse namespace.

Quando eu defino uma função, ela está no namespace `__main__`, mas ela cria um novo namespace local da função. Assim, posso ter um mesmo nome `a` nos dois namespaces, apontando pra dois objetos diferentes. E chamamos de **escopo** a parte do texto onde eu posso acessar os nomes de um namespace.

O escopo de uma função então nada mais é do que a parte interna da função, onde o namespace dela pode ser acessado, e consequentemente as variáveis dela.

## Variáveis

Assim, se eu defino uma variável dentro do **escopo** de uma func, ela está sendo escrita no **namespace** dessa func. Uma variável dentro do escopo de uma func normalmente não é acessível fora desse escopo, justamente por estar em um namespace diferente. Então uma variável na `func_1` não pode ser acessada pela `func_2` de formal convencional, diferente de uma variável no escopo global, que pode ser acessível pelas duas. Chamamos essa variáveis definidas dentro de funcoes de **variável local**.

```python
a = 1 # global var

func_1():
    b = 2 # local var
    print(a, b) # 1, 2
    
func_2():
    c = 3 # local var
    print(a, c) # 1, 3
    
func_3():
    print(a) # 1
    print(b) # NameError: name 'b' is not defined
    print(c) # NameError: name 'c' is not defined
```

Repare: todas as funcs tinham acesso a variável `a` mesmo sem essa var ter sido passada como parâmetro, pois ela é uma variável global. Mas tanto `b` quanto `c` estão sendo definidas dentro de funções, então estão apenas no namespace das suas respectivas funções, e o namespace tentando acessar `b` e `c` não possui esses nomes. Sendo assim, não consigo acessar elas fora de suas funções.

Mas temos um detalhe importante pro que estamos fazendo aqui: funcs internas têm acesso de *leitura* aos namespaces das funções externas. Internamente, ele procura primeiro no namespace local, e depois vai subindo o namespace até encontrar a variável. Ex.:

```python
def soma_x(var_ext):
    def func_int(var_int):
        return var_ext + var_int
    return func_int

soma_1 = soma_x(1)
soma_10 = soma_x(10)
soma_1(10) # 11
soma_10(10) # 20
```

Aqui, eu defino uma **funcao de ordem superior**, que me retorna uma funcao. Essa nova funcao sempre soma com um valor fixo que passei pra func de ordem superior.

Mas repare no detalhe: a `func_int` acessa a `var_ext`, mesmo sem ter recebido ela como parâmentro. Isso pq `func_int` tem acesso de *leitura* ao namespace da `func_ext`. Assim, `func_int` consegue ler o valor de `var_ext`, mesmo `var_ext` não estando no escopo da `func_int`.

Chamamos essa `func_int` de **CLOSURE**
