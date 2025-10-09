from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('eco/<str:message>/', views.eco, name='eco'),
    path('info/', views.info, name='info'),

    path('home/', views.home, name='home'),
    path('conditionals/', views.conditionals, name='conditionals'),

]