from django.shortcuts import render
from produtos.models import Produtos

def home(request):
    return render(request, 'home.html')


def cad_produtos(request):
    return render(request, 'cad_produtos.html')


def ver_produtos(request):
    search = request.GET.get('search')
    dt_produtos = Produtos.objects.all() 

    if search:
        dt_produtos = Produtos.objects.filter(nome=search) or Produtos.objects.filter(tipo=search)

    return render(
        request, 
        'ver_produtos.html',
        {'produtos': dt_produtos}
        )