from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
#from django.views import View

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

# class EcoView(View):
#     def eco(request, message):
#         return HttpResponse(f"Você digitou: {message}")