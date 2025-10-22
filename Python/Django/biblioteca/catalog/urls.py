# filepath: c:\Users\anand\git\Practices\Python\Django\biblioteca\catalog\urls.py
from django.urls import path
from django.http import HttpResponse

def index(request):
    return HttpResponse("Biblioteca: catálogo")

urlpatterns = [
    path('', index, name='catalog-index'),
]