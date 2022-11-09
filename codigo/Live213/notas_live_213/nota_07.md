# Closures

Uma **closure** é uma funcao que definida e retornada por uma outra funcao.

A grande saca da Closure é que nomes em seu namespace são preservados, como vimos anteriormente. Ou seja, as variáveis de "fora" da funcao interna também sao preservadas. Então temos uma fábrica de funcoes!

Vamos fazer um exemplo básico: um contador!

```python
def contador(start=0):
    count = start
    def interna():
        count += 1
        return count
    return interna

c = contador()
print(c()) # 1
print(c()) # 2
```

Beleza, agora sempre que eu chamar a func, ela incrementa um. Porém, temos aqui um erro! Vamos refazer essa closure, mas anotando os escopos:

```python
# Escopo global
var_global=1

def contador(start=0): # Global
    
    # Escopo local de contador
    count = start # Local
    def interna(): # Local
        # Escopo local da interna
        outra_var = 'var' # local
        
        count += 1 # local ou global?
        
        return count
    return interna
```

Aqui, podemos ver que é simples definir de qual escopo cada variável faz parte. `outra_var` por exemplo está no escopo local da `interna`, e nao faz parte do escopo da `contador`. Mas, `count` estava no escopo de `contador`, e está sendo acessada dentro da `interna`... Então de qual escopo ela faz parte quando chamamos ele na `interna`? Local ou Global?

Essa pergunta na verdade é uma pegadinha: `count` não está nem no escopo local da minha func, e nem no escopo global. Ela tá num limbo, entre o escopo global, e o escopo da minha func: o escopo da func acima, a funcao `contador`!

Perceba que é diferente do exemplo na nota anterior sobre escopo de variáveis: `count` não é uma variável sendo passada pra funcao `contador`. Ela está sendo *definida dentro* da funcao `contador`. Por isso ela não está acessível, pq a funcao `interna` não tem acesso de escrita ao namespace da `contador`, apenas acesso de leitura!

Então, como eu resolvo esse problema? Usando a palvra mágica `nonlocal`. Ela é uma palavra específica pra Closures que serve pra eu indicar pro python que ele precisa procurar por essa variável no namespace *ACIMA* do escopo que está sendo executado no momento. Então, o código correto e sem bugs ficaria:

```python
def contador(start=0):
    count = start
    def interna():
        nonlocal count
        count += 1
        return count
    return interna

c = contador()
print(c()) # 1
print(c()) # 2
```

Chamamos `count` agora de **variável livre** (freevar). Agora ela não pertence nem ao escopo Local e nem ao Global, mas tem um escopo livre, pois está sendo acessada e modificada em outros escopos.
