from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")
def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
def Dominik(request):
    return HttpResponse("Hola Dominik")
def Alexis(request):
    return HttpResponse("Hola Alexis")