from rest_framework.routers import DefaultRouter

from .views import LivrosViewSet

router = DefaultRouter()
router.register(r'', LivrosViewSet, base_name='livros')

livros_urls = router.urls
