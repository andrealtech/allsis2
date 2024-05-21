from django.urls import path
from produtos.views import cad_produtos, ver_produtos

urlpatterns = [
    path('cad_produtos/', cad_produtos, name='cad'),
    path('ver_produtos/', ver_produtos, name='ver'),
]
