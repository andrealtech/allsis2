from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def cad_produtos(request):
    return render(request, 'cad_produtos.html')


def ver_produtos(request):
    return render(request, 'ver_produtos.html')