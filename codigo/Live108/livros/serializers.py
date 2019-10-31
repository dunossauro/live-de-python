from .models import Livro, Categoria
from rest_framework import serializers


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class LivrosSerializer(serializers.ModelSerializer):
    disponivel = serializers.ReadOnlyField()

    class Meta:
        model = Livro
        exclude = ['em_estoque']