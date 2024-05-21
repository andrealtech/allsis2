from django.shortcuts import render


def servicos(request):
    return render(request, 'ver_servico.html', {'servicos': {'descrição':'manutenção'}})