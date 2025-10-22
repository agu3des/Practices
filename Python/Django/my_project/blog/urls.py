from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('contato/<str:telefone>/', views.contato, name='contato'),
    path('about/', views.about, name='about'),
    path('conditionals/', views.conditionals, name='conditionals'),
    path('loops/', views.loops, name='loops'),  # Nova URL
]