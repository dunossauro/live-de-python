# Funções aninhadas

São funções definidas dentro de outras funções.

```python
def ola(nome):
    def func_intera(nome):
        if nome.lower() == 'marilene':
            print(f'Olá, {nome}. Hoje a noite...')
        else:
            print(f'Olá, {nome}, boas vindas!')
            
    func_interna(nome)
```

Ok, muito bacana... mas pra que eu quero essa funcionalidade? Temos algumas situações onde isso pode ser útil:

- Funções ajudantes
  - Evitar repetição de código dentro da func superior
  - Colocar toda a complexidade num lugar só
- Encapsulamento
  - Escopo da func interna não é acessível fora da função
- Escopo de variáveis
  - A func interna pode utilizar as variáveis da func superior

Pra dar um exemplo prático, vamos começar com esse código abaixo, que normaliza um texto (remove todos os acentos nesse caso).

```python
from uincodedata import normalize

def normaliza(*palavras):
    saida = []
    for palavra in palavras:
        normalizado = normalize('NFKD', palavra)
        narmalizada = normalizado.encode('ASCII', 'ignore').decode('ASCII')
        saida.append(normalizada)
    return saida

normalizada('Érico', 'Cássio', 'Cíçero')
# ['Erico', 'Cassio', 'Cicero']
```

Wow. Que puta for complexo né, com bastante passos e um pouco complexo de ler... E um for dentro de uma função ainda, me parece uma lógica meio convoluta. Posso simplificar isso botando toda a parte complexa pra dentro de uma função ajudante.

```python
from uincodedata import normalize

def normaliza(*palavras):
    def remove_acentos(palavra):
        normalizado = normalize('NFKD', palavra)
        return normalizado.encode('ASCII', '`ignore').decode('ASCII')
        
    return [remove_acentos(palvra) for palavra in palavras]

normalizada('Érico', 'Cássio', 'Cíçero')
# ['Erico', 'Cassio', 'Cicero']
```

Aqui, a leitura fica mais fácil. Eu não preciso compreender completamente cada passo complexo da func ajudante. Eu sei que ela está removendo os meus acentos. E eu depois removo os acentos pra cada palavra na lista de palavras. E pronto!! Essa func pra remover acentos está *encapsulada*. Eu não quero que mais pessoas saiam chamando essa func no resto do código. Nesse caso, pq lida com conversão de encoding (que pode dar dor de cabeça), mas pode ser pq é uma func que lida com senhas ou outros dados sensíveis.
