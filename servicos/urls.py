from django.urls import path
from servicos.views import servicos

urlpatterns = [
    path("ver_servicos/", servicos, name='serv')
]