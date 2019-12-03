## Projeto demo (básico) sobre testes de performance com Python e Locust
Este projeto possui uma api com serviços criados estrategicamente para treinar a criação de testes de performance.

Endpoints disponíveis:

#### /get-auth
É necessário passar o seguinte body para obter o 'auth': {"pass": "1234"}. Este post retorna um json com o código 'auth' e configura o cookie 'auth'.

#### /nao-autorizado-cookie
Caso o cookie 'auth' não esteja configurado na sessão, haverá redirecionamento para /redirected.
Para testar sem redirecionamento é necessário estar autenticado.
Para autenticar execute o post 'get-auth' acima.

#### /nao-autorizado-param
Caso o param 'auth' não seja informado (com o token gerado pelo 'get-auth'), haverá redirecionamento para /redirected.
Para obter o token 'auth', execute o post 'get-auth' acima.

#### /get-complex-object
Este endpoint retorna um objeto complexo quando passado o argumento 'returnObject': 'True'


## Instalando dependências
pip install -r requirements.txt

## Executando API de teste
```bash
cd demo _server
./run_server
```

## Iniciando Locust
```bash
locust -f _locust/usuario_api.py
```

## Iniciando execução dos testes
* Acesse http://localhost:8089
* Inicie execução dos testes
