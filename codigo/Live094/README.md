# live94-django

Repo for Live de Python 94 - Django


## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/dunossauro/live-de-python.git
cd live-de-python/codigo/Live94
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --username='admin'
python manage.py runserver
```

Repositório original: https://github.com/rg3915/live94-django


## Criando um banco PostgreSql

```
sudo su - postgres
createdb live94
createuser -P dunossauro
pass: 94
psql live94
GRANT ALL PRIVILEGES ON DATABASE live94 TO dunossauro;
\q
exit
```

## Criando a pasta templates

```
mkdir -p myproject/core/templates/includes
touch myproject/core/templates/{base,index}.html
touch myproject/core/templates/includes/nav.html
```

https://gist.github.com/rg3915/0144a2408ec54c4e8008999631c64a30

## Criando um novo app

```
cd myproject
python ../manage.py startapp live
cd ..
tree
touch myproject/live/urls.py
mkdir -p myproject/live/templates/live
touch myproject/live/templates/live/live_{list,detail,form}.html
```


### Herança de templates

```html
{% extends "base.html" %}
```

## Forms e CreateView

```
touch myproject/live/forms.py
```

## Criando comandos personalizados

```
mkdir -p myproject/core/management/commands
touch myproject/core/management/__init__.py
touch myproject/core/management/commands/{__init__,import_lives}.py
```

O comando criado pode ser rodado com

```
python manage.py import_lives
```

## ORM

```
lives = Live.objects.all()
lives.count()

lives_like = Live.objects.filter(like__lte=1000)
lives_like.count()

lives_python = Live.objects.filter(title__icontains='python')
lives_python.count()

lives_no_python = Live.objects.exclude(title__icontains='python')
lives_no_python.count()

Live.objects.filter(like__lte=1000).values('title', 'guest')
Live.objects.filter(like__lte=1000).values_list('title', 'guest')
Live.objects.filter(like__lte=1000).values_list('title', flat=True)
```

---

```
from django.db import connection

lives = Live.objects.all()

for live in lives:
    print(live.guest)

print(len(connection.queries))
```

---

```
from django.db import connection

lives = Live.objects.select_related('guest').all()

for live in lives:
    print(live.guest)

print(len(connection.queries))
```

---

http://pythonclub.com.br/django-introducao-queries.html

---

### Inserindo dados

```
from django.db import connection


lives = [
    'Testes de unidade na prática',
    'Melhorando testes de unidade',
    'Testando o que está pronto',
    'Autenticação de uma API Flask com testes',
    'BDD com python e flask',
    'Type hints e Anotações de funções',
    'Django básico',
    'Django parte 2',
]

for i, live in enumerate(lives):
    Live.objects.create(title=live, number=i)

print(len(connection.queries))
```

---

```
from django.db import connection


lives = [
    'Testes de unidade na prática',
    'Melhorando testes de unidade',
    'Testando o que está pronto',
    'Autenticação de uma API Flask com testes',
    'BDD com python e flask',
    'Type hints e Anotações de funções',
    'Django básico',
    'Django parte 2',
]

aux = []
for i, live in enumerate(lives):
    obj = Live(title=live, number=i)
    aux.append(obj)

Live.objects.bulk_create(aux)

print(len(connection.queries))
```


---

Obs: Em bulk_create os signals do Django não serão chamados.


## Filtrando campos calculados

```
res = [x.pk for x in Live.objects.all() if x.like_frequence < 0.2]
len(res)
```

## Links

[Tutorial Django 2.2](http://pythonclub.com.br/tutorial-django-2.html)

[Django doc oficial](https://www.djangoproject.com/)

[diagrama 1](https://raw.githubusercontent.com/rg3915/tutoriais/master/django-basic/img/diagrama.png)

[diagrama 2](https://raw.githubusercontent.com/rg3915/tutoriais/master/django-basic/img/mtv2.png)

[env_gen.py](https://gist.github.com/rg3915/22626de522f5c045bc63acdb8fe67b24)

[gist básico para criar os templates base.html e index.html](https://gist.github.com/rg3915/0144a2408ec54c4e8008999631c64a30)

[CBV](https://ccbv.co.uk)

[djangopackages](https://djangopackages.org/)

[QuerySet API reference](https://docs.djangoproject.com/en/1.11/ref/models/querysets/)

[Como otimizar suas consultas no Django - De N a 1 em 20 minutos](http://pythonclub.com.br/django-introducao-queries.html)

[Visualizando query SQL a partir do ORM Django](https://medium.com/@beatrizuezu/visualizando-query-sql-a-partir-do-orm-django-5771370a9c55)

[Django ORM optimization story on selecting the least possible](https://www.peterbe.com/plog/django-orm-optimization-story-on-selecting-the-least-possible)

