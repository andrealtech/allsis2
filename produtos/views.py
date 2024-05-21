from django.shortcuts import render
from produtos.models import Produtos

def home(request):
    return render(request, 'home.html')


def cad_produtos(request):
    return render(request, 'cad_produtos.html')


def ver_produtos(request):
    
    dt_produtos = Produtos.objects.all()

    return render(
        request, 
        'ver_produtos.html',
        {'produtos': dt_produtos}
        )