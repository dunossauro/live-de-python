Funcionalidade: API


Cenário: Resposta do mapa da API
  Quando faço uma requisição na url "/"
  Então a api deve responder
  """
  {"artistas": "url/artistas", "albuns": "url/albuns"}
  """

Cenário: Requisição de artistas na API
  Quando faço uma requisição na url "/artistas"
  Então a api deve responder
  """
  {}
  """


Cenário: Inserção de um artista na API
  Quando faço uma requisição POST na url "/artista"
   """
   {"nome": "Zimbra"}
   """
  Então a api deve responder
  """
  {
    "201 Created": {
        "nome": "Zimbra"
    }
  }
  """
  Quando faço uma requisição na url "/artistas"

  Então a api deve responder
  """
  {
    "1": "zimbra"
  }
  """

@solo
Cenário: Inserção de um disco na API
  Quando faço uma requisição POST na url "/album"
   """
   {
     "nome": "Vem",
     "artista":"Mallu",
     "ano": 2017
   }
   """
