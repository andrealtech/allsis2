from django.contrib import admin
from django.urls import path, include
from produtos.views import home 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('produtos/', include('produtos.urls')),
    path('servicos/', include('servicos.urls')),
]
