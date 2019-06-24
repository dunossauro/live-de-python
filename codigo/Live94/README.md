# live94-django

Repo for Live de Python 94 - Django


## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/live94-django.git
cd live94-django
python3 -m venv .venv
source .venv/bin/activate
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

## Filtrando campos calculados

```
res = [x.pk for x in Live.objects.all() if x.like_frequence < 0.2]
len(res)
```

