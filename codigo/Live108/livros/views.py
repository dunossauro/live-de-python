from rest_framework import viewsets
from .serializers import LivrosSerializer

from .models import Livro


class LivrosViewSet(viewsets.ModelViewSet):
    serializer_class = LivrosSerializer
    queryset = Livro.objects.all()
