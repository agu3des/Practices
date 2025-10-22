from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import date, datetime

def welcome(request):
    return HttpResponse("Welcome to the Blog!")

def eco(request, message):
    return HttpResponse(f"Você digitou: {message}")

def info(request):
    data ={
      "disciplina": "RAD",
      "framework": "Django",
      "semestre": "2025.2"
    }
    return JsonResponse(data)

def home(request):
    contexto = {
        "usuario": "Ananda",
        "now": date.today(),
        "numero_original": 15,  
    }
    return render(request, "home.html", contexto)

def conditionals(request):
    context = {
        'is_logged_in': True,
        'idade': 20,
        'role': 'admin'
    }
    return render(request, 'conditionals.html', context)

def home(request):
    context = {
        'username': 'João',
        'number': 42,
        'now': datetime.now(),
        'is_logged_in': True,
        'idade': 20,
        'role': 'admin',
        'produtos': [
            {'nome': 'Laptop', 'preco': 3500.00},
            {'nome': 'Mouse', 'preco': 120.00},
            {'nome': 'Teclado', 'preco': 250.00}
        ]
    }
    return render(request, 'home.html', context)

def contato(request, telefone):
    return render(request, 'contato.html', {'telefone': telefone})

def about(request):
    return render(request, 'about.html')

def loops(request):
    context = {
        'produtos': [
            {'nome': 'Laptop', 'preco': 3500.00},
            {'nome': 'Mouse', 'preco': 120.00},
            {'nome': 'Teclado', 'preco': 250.00}
        ]
    }
    return render(request, 'loops.html', context)



