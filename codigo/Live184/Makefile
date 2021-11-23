TEST_TARGET=teste.py
POETRY = poetry run
FLAKE8_FLAGS = --ignore=W503,E501
ISORT_FLAGS = --profile=black --lines-after-import=2


## @ instalacao
.PHONY: instalar
instalar: ## instala programa usando poetry, poetry precisa estar instalado
	poetry install

## @ programa 
.PHONY: rodar
rodar: saida.txt ## roda programa verificando dependencias em programa.py e entrada.txt
saida.txt: programa.py entrada.txt
	${POETRY} python programa.py

## @ testes
.PHONY: teste cobertura
teste: ## Roda teste
	${POETRY} pytest ${TEST_TARGET}
cobertura: ##roda cobertura de testes
	${POETRY} pytest --cov=. --cov-report=html $(TEST_TARGET)

## @ analise
.PHONY: lint_black flake mypy lint_isort analise
lint_black:
	${POETRY} black --check .
flake:
	${POETRY} flake8 ${FLAKE8_FLAGS} .
mypy:
	${POETRY} mypy .
lint_isort:
	${POETRY} isort ${ISORT_FLAGS} --check .
analise: lint_black flake mypy lint_isort ## roda analise estatica: black, flake, mypy e isort

## @ formatacao
.PHONY: black isort formatar
black:
	${POETRY} black .
isort:
	${POETRY} isort ${ISORT_FLAGS} .
formatar: isort black ## roda formatacao nos arquivos da pasta usando black e isort

.PHONY: ajuda
ajuda:
	@${POETRY} python ajuda.py
