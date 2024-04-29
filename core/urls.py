from django.contrib import admin
from django.urls import path
from produtos.views import home, cad_produtos, ver_produtos
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('cad_produtos/', cad_produtos),
    path('ver_produtos/', ver_produtos),
    #path('blog/', include('blog.urls'))
]
