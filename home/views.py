from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return HttpResponse ("<h1>Sistema 1.0 desenvolvido por mim mesmo.<h1>")

def contato(request):
    return HttpResponse ("Esta é a página de contato")

def ajuda(request):
    return HttpResponse ("Esta é a página de ajuda")