# language:pt

Funcionalidade: Saber as tarefas que tenho a realizar
  """
  Seja eu uma pessoa interessante.
  Quero saber quais tarefas tenho para fazer
  """
  Cenário: No primeiro uso do sistema não devem existem tarefas registradas
    Quando verificar minhas tarefas em "/tasks"
    Então não devo ter nenhuma tarefa para fazer

  Cenário: Ver tasks registradas
    Dado que exista uma tarefa
     | nome      | descriação | estado |
     | toma ping | pq é bom   | false  |
    Quando verificar minhas tarefas em "/tasks"
    Então não devo ter nenhuma tarefa para fazer
     | nome      | descriação | estado |
     | toma ping | pq é bom   | false  |