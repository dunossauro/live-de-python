# Uma introdução a Internacionalização (I18n) e Localização (L10n) | Live de Python #290


i18n -> Ter um software que possui algumas características para que possa existir a L10N
l10n -> Conversar com pessoas de diferentes culturas

---

GNU gettext (padrão do python)

/locale
  / ISO 639-1 (set 1) _ ISO 3166-1 (alpha 2) -> `pt_BR`
    / LC_MESSAGES
      / messages.mo
	

## Gerando os arquivos de tradução

```bash
xgettext -o messages.pot exemplo_00.py  # geramos o pot
msginit --locale=pt_BR.UTF-8 --input=messages.pot --output=pt_BR.po  # po
msgfmt pt_BR.po -o locale/pt_BR/LC_MESSAGES/messages.mo  # mo
msgunfmt locale/pt_BR/LC_MESSAGES/messages.mo
msgmerg -U pt_BR.po messages.pot
```

## Olá mundo

```python
import gettext

t = gettext.translation(
    'messages', localedir='locale', fallback=True
)

t.install()

print(_('Hello'))
```

---

## Pacotes com .mo

```toml
# Exemplo setuptools
[tool.setuptools.packages.find]
where = ["pacote"]

[tool.setuptools.package-data]
"*" = ["*.mo"]
```

## Windows!

gettext para windows: https://github.com/mlocati/gettext-iconv-windows


## Glossario

.pot: Portable Object Template
.po: Portable Object
.mo: Machine Object


## TODO

- Internacionalização (Carece de verbete, referencia e explicação)
  - Verbete: w3c
  - Referência: Nielsen (Designing user interfaces for international use) / FreeStandardGroup
  - Explicação: w3c / gettext / FreeStandardGroup
- Localização (Carece de verbete, referencia e explicação)
  - Verbete: w3c
  - Referência: Uren et al. (Software internationalization and localization: an introduction)
  - Explicação: w3c


## Roteiro parcial

0. Avisos
   - Python puro
   - Sem interfaces
   - Sem web
   - Um introdução ao assunto
1. Explicar a importância de regionalizar software
2. Entrando no buraco de coelho
   - Linhas de texto
	 - PT: Esquerda pra direita
	 - AR: Direita pra esquerda
	 - JP/KO: Colunas esquerda pra direita
   - Datas
   - Números
	 - . e ,
	 - Arábicos (base 12)
   - Pluralização
     - Formas do singular
	 - Formas plurais
3. Explicar a diferença entre i18n e l10n
4. Mostrar o padrão GNU gettext (o usado pelo python)
   - gettext vs windows
5. Apresentar o glossário (.pot, .po e .mo)
6. Montar um "Olá mundo" "internacionalizavel"
7. Empacotamento (um slide com exemplo)
8. Pacotes externos que podem ajudar (humanize, babel, [sualib]-i18n)


## Um esquema básico

```mermaid
i18n --> gettext
i18n --> locale
```


### Internacionalização

"Internacionalização é o processo de generalizar um produto para que ele possa lidar com múltiplos idiomas e convenções culturais sem a necessidade de redesign. A internacionalização ocorre no nível do design do programa e do desenvolvimento de documentos."

Localization Industry Standards Association (LISA)

### Localização

"A localização envolve pegar um produto e torná-lo linguisticamente e culturalmente apropriado para o local de destino (país/região e idioma) onde ele será usado e vendido."

Localization Industry Standards Association (LISA)

> Localization Industry Standards Association (LISA) - Consorcio de empresas discutiram sobre o tema entre 1990 e 2011.


---

> TODO: Procurar sobre a spec do wasm em relação ao POSIX
> TODO: Olhar o https://gitlab.pyicu.org/main/pyicu



---


> TODO Montar um exemplos de Babel
> TODO Montar um exemplo com Pint
