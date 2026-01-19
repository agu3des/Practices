from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, EditoraViewSet, LivroViewSet, PublicaViewSet

# Criar router para registrar os viewsets
router = DefaultRouter()
router.register(r'autores', AutorViewSet, basename='autor-api')
router.register(r'editoras', EditoraViewSet, basename='editora-api')
router.register(r'livros', LivroViewSet, basename='livro-api')
router.register(r'publicacoes', PublicaViewSet, basename='publica-api')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
