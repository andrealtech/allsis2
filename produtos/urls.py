from django.urls import path
from produtos.views import cad_produtos, ver_produtos, cad_tipos

urlpatterns = [
    path('cad_produtos/', cad_produtos, name='cad'),
    path('cad_tipos/', cad_tipos, name='cad_tipos'),
    path('ver_produtos/', ver_produtos, name='ver'),
]
