# Definindo o contexto

Como dito na nota anterior, vou agora documentar todas as pequenas partes do python que a gente precisa entender pra conseguir no final aplicar tudo junto e entender os decoradores

## Um mar de nomes

- Decoradores são um **açúcar sintático** para o funcionamento de **closures**
- **Closures** são um caso especial de **aninhamento de funções** de **ordem superior**, que armazenam **variáveis livres**
- **Funções Aninhadas** são funções definidas dentro de funções
- **Funções de ordem superior** quer dizer que a função pode receber ou retornar **funções de primeira classe**
- **Funções de primeira classe** são funções como objetos. Podem ser colocadas em variáveis, passadas/retornadas por outras funcs, ou colocadas em contêineres
- **Variáveis livres** são variáveis que não pertencem ao escopo local ou global

Sim, é bastante coisa, mas vamos por partes que a gente chega lá! Eu vou seguir uma abordagem de baixo pra cima: primeiro o conceito mais básico, e depois a gente vai subindo. A orde de abordagem vai ser:

- Funções de primeira classe
- Funções de ordem superior
- Aninhamento de Funções
- Variáveis livres
- Closures
- Decoradores
