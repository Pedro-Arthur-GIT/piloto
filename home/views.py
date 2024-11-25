from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest

# Create your views here.

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def ajuda(request):
    return render(request, 'ajuda.html')

def exibir_item(request, id):
    return render(request, "exibir_item.html", {'id': id})
 
def perfil(request, usuario):
    return render(request, "perfil.html", {'usuario' : usuario})

def dia_semana(request, dia):

    dias_da_semana = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }

    if dia in dias_da_semana:
      
        nome_do_dia = dias_da_semana[dia]
        return render(request, "dia_semana.html", {'dia': nome_do_dia})
    else:

        return HttpResponseBadRequest("<h1>Número inválido. Por favor, insira um número de 1 a 7.</h1>")
    
     