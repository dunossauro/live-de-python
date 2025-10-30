---
título: Servidores de aplicação e especificações (WSGI / ASGI)
---

Roteiro:

1. Desmembrando uma aplicação web
  - Cliente / Servidor: Arquitetura da web
    - HTTP e suas versões
  - Servidor web -> Servidor de Aplicação -> Aplicação
    - Delegando as responsabilidades
	  - Servidor web
	  
2. Servidor de aplicação
  - O que são?
  - Qual a função?
  - Quando usar?
  - Em outras linguagens
  - Especificações
	- WSGI (PEP 333, PEP 3333)
	- ASGI (No PEP)
  - Os servidores python (criar tabelas de spec vs http versions)
    - WSGI
      - Gunicorn
	  - uWSGI
	  - Granian
	- ASGI
      - Granian
	  - Uvicorn
	  - HyperCorn

3. A Aplicação

- Criar o DunnoFramework
  - Utilizar em algum projeto simples
