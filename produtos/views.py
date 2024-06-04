from django.shortcuts import render, redirect
from produtos.models import Produtos
from produtos.forms import ProdutoForm, TipoProdutoForm

def home(request):
    return render(request, 'home.html')


def cad_tipos(request):
    if request.method == 'POST':
        new_tipos = TipoProdutoForm(request.POST)  
        if new_tipos.is_valid():
            new_tipos.save()
            return redirect('cad')
    else:
        new_tipos = TipoProdutoForm()
    return render(request, 'cad_tipos.html', {'new_tipos': new_tipos})


def cad_produtos(request):
    if request.method == 'POST':
        new_produtos = ProdutoForm(request.POST)
        if new_produtos.is_valid():
            new_produtos.save()
            return redirect('ver')
    else:
        new_produtos = ProdutoForm()
    return render(request, 'cad_produtos.html', {'new_produtos': new_produtos})



def ver_produtos(request):
    search = request.GET.get('search')
    dt_produtos = Produtos.objects.all() 
    if search:
        dt_produtos = Produtos.objects.filter(nome=search) or Produtos.objects.filter(tipo=search)
    return render(
        request, 'ver_produtos.html', {'produtos': dt_produtos})