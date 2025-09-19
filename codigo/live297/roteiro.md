---
título: Arquitetura de MicroKernel / Sistema de plugins com Pluggy
número: 297
---

Roteiro:

1. Descrevendo a arquitetura
    - Definição
	- Exemplos
	- Topologia
	    - Core
	    - Registers / Contratos (API)
	- Problemas que ela resolve
	- Como conseguir isso
		- importlib (JP) / stevedore / Pluggy

2. Apresentar o pluggy
    - Apresentação
	- Quem usa o pluggy
	- Manager / Register / Hooks
	- Criar um plugin de exemplo
        - Classes
		- Funções
	- Plugins externos (instaláveis)
		- `pyproject.toml`
        - `load_setuptools_entrypoints`

3. Prática
    - Montar um exemplo prático!
	- Factory
	- Algumas dicas:
	    - OCP - Open/Closed Principle
    	- Padrões wrappers (adapter/proxy/decorator)

4. trade-off
    - Pluggy
        - Gerenciamento de configuração
    	- Lazy load
    - Arquitetura
        - ...
