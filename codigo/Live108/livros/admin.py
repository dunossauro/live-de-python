from django.contrib import admin

from .models import Livro, Categoria

admin.site.register([Livro, Categoria])
