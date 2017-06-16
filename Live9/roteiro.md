# Uma introdução teórica

## TCP-IP e protocolos (Um blá sobre redes)

Temos 7 camadas no protocolo ISO ![]() e o equivalente em 4 camadas no modelo TCP/IP, mas vamos falar um pouco somente sobre a camada de aplicação no TCP/IP.

- **4**. Aplicação
- **3**. Transporte
- **2**. Rede
- **1**. Física

Mas um resumo breve sobre as camadas

- Física: é uma espécie de interface padrão para todos os dispositivos

- Rede: É a camada que da nome aos bois, relaciona endereços de rede (ip) com indentificadores únicos (MAC) .. (IP, ICMP, ARP e ...) Quem e onde?

- Transporte: Cordenação de envio, integridade, quebra dos pacotões em pacotinhos ... (UDP/TCP)

#### Aplicação

É a camada palpável. Imagine uma chamada de página web. Eu digo ao browser (minha aplicação), que acesse a página `www.page.com` Então, por meio de um protocolo de aplicação, no caso HTTP, a pacote será particionado a camada de transporte, por meio do protocolo TCP que irá localizar o nó de rede pela camada de rede e o pacote usará a interface padrão definida na camada física para ser transportado.

#### HTTP
É um protocolo de comunicação, que trabalha na camada de aplicação

#### Cookies
Não, não são biscoitos..

São grupos de dados, pense em uma pequena tabelinha, entre o servidor web e o seu navegador. Normalmente essa tabela contém 5 campos

|Domínio| Path| Content| Expires| Secure|
|-|-|-|-|-|
|meusite.com|/|User=eduardo|15 de outubro de 2030 7:00|Yes|

**cola**
- Domínio: De onde vem o cookie
- Path: O caminho no diretório em que o servidor identifica os arquivos que podem usar o cookie (geralmente / pra todo mundo)
- Content: chave=valor; Geralmente uma string simples com um valor correspondente
- Expires: Adiciona a data de expiração do cookie (caso não haja o cookie será deletado ao encerramento do browser)
- Secure: Bool, define se o cookie é seguro ou não.


## Verbos
Quando se pensa em acessar páginas, urls, existem diferentes tipos de chamadas/requisições que denominamos verbos

|verbo| o que faz?|
|-|-|
|GET|É o método que pede um recurso ao servidor|
|POST|Envia informações para a criação de um novo recurso|
|PUT|Edita as informações de um determinado recurso|
|DELETE|Solicita a remoção de um recurso|

# Códigos de retorno

- 1xx: Enviar informações para o cliente de que sua requisição foi recebida e está sendo processada
- 2xx: Indica que a requisição do cliente foi bem sucedida
- 3xx: Informa a ação adicional que deve ser tomada para completar a requisição
- 4xx: Avisa que o cliente fez uma requisição que não pode ser atendida
- 5xx: Ocorreu um erro no servidor ao cumprir uma requisição válida.

## Rotas
As rotas são o que definem as URLS, por exemplo, quando você precisa pagar uma conta, você pode usar: `www.banco.com.br/pagamentos`. Ou também `www.banco.com.br/pagamento_de_contas`. Isso torna o mapeamento do sistema mais previsível e caso os usuários pretendam navegar diferetamente aquele lugar do site, podem redirecionar seu navegador a rota específica.

Existem rotas dinâmicas e rotas estáticas, o que isso quer dizer? Rotas estáticas, como próprio nome diz, são rotas que não variam e sempre exibem o mesmo comportamento.

Já as rotas dinâmicas podem ser 'customizaveis'. Imagine que você é um usuário administrador do sistema `www.seusite.com/<usuario>`, vamos pensar que cada usuário do seu sistema pode usar sua própria pagina, porém a página renderizada para cada usuário pode ser diferente.

# Bottle

Bottle é um micro-framework web construído em um único arquivo e que não tem dependencias de outras bibliotecas

- Routing: Requests to function-call mapping with support for clean and dynamic URLs.

- Templates: Fast and pythonic built-in template engine and support for mako, jinja2 and cheetah templates.

- Utilities: Convenient access to form data, file uploads, cookies, headers and other HTTP-related metadata.

- Server: Built-in HTTP development server and support for paste, fapws3, bjoern, gae, cherrypy or any other WSGI capable HTTP server.

## fontes
[RFC HTTP](https://tools.ietf.org/html/rfc2616)

[Documentação oficial](http://bottlepy.org/docs/dev/index.html)

[Tutorial oficial](http://bottlepy.org/docs/dev/tutorial.html)
