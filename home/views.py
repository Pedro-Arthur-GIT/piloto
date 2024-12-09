from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from .forms import ContatoForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    form = ContatoForm()
    contexto = {
        'form': form,
    }
    return render(request, 'contato.html', contexto)

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
    

def produtos(request):
    contexto = {
        'lista': [
            {'id': 1, 'nome': 'Notebook', 'preco': '2.500,00'},
            {'id': 2, 'nome': 'Monitor', 'preco': '500,00'},
            {'id': 3, 'nome': 'Teclado', 'preco': '80,00'},
            {'id': 4, 'nome': 'Mouse', 'preco': '40,00'},
            {'id': 5, 'nome': 'Impressora', 'preco': '600,00'},
            {'id': 6, 'nome': 'Scanner', 'preco': '700,00'},
            {'id': 7, 'nome': 'Câmera Web', 'preco': '150,00'},
            {'id': 8, 'nome': 'Headset', 'preco': '120,00'},
            {'id': 9, 'nome': 'Pendrive 32GB', 'preco': '30,00'},
            {'id': 10, 'nome': 'HD Externo 1TB', 'preco': '350,00'},
            {'id': 11, 'nome': 'Estabilizador', 'preco': '200,00'},
            {'id': 12, 'nome': 'Switch 8 portas', 'preco': '180,00'},
            {'id': 13, 'nome': 'Roteador Wi-Fi', 'preco': '220,00'},
        ],
    }
    return render(request, 'produto/lista.html',contexto)  

def form_prod(request):
    return render(request, 'produto/form_prod.html')

     