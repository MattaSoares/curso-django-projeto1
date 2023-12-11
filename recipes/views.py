from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Mateus Soares',
    })


def sobre(request):
    return HttpResponse('Novo Sobre')


def contato(request):
    return render(request, 'recipes/contato.html')

