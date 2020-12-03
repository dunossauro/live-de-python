from django.db import models


class Todo(models.Model):
    title = models.CharField("Título", max_length=50)
    description = models.TextField("Descrição")
    done = models.BooleanField(default=False)
