from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import date

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
    contexto = {
        "loggin_in": False, 
        "idade": 15,
        "role": "admin",
    }
    return render(request, "conditionals.html", contexto)



