# language:pt


Funcionalidade: Cadastro
Cenário: Efetuar cadastro com sucesso
 Dado que o usuario esteja na pagina "http://localhost:8080/cadastro"
 Quando inserir o "nome" "Eduardo"
 E inserir o "sobrenome" "Mendes"
 E inserir o "usuario" "z4r4tu5tr4"
 E inserir o "sexo" "Masculino"
 E inserir o "senha" "1234567"
 E inserir o "email" "mendesxeduardo@gmail.com"
 E inserir o "nascimento" "06/03/1993"
 Então clicar no botão "Enviar"
 E a mensagem deverá ser exibida
  """
  Bem vindo Eduardo
  Usuário: z4r4tu5tr4
  Senha: 1234567
  """


Cenário: Efetuar cadastro com senha inváida
Dado que o usuario esteja na pagina "http://localhost:8080/cadastro"
Quando inserir o "nome" "Eduardo"
E inserir o "sobrenome" "Mendes"
E inserir o "usuario" "z4r4tu5tr4"
E inserir o "sexo" "Masculino"
E inserir o "senha" "123"
E inserir o "email" "mendesxeduardo@gmail.com"
E inserir o "nascimento" "06/03/1993"
Então clicar no botão "Enviar"
E a mensagem deverá ser exibida
"""
Senha inválida, use ao menos 6 caracteres
"""
