from django.contrib import admin
from django.urls import path
#se importa abajo la union entre el archivo creado vista con esta pagina
from myproject.vista import index
urlpatterns = [
    path('admin/', admin.site.urls),
    #abajo encontramos el enlace web con el proyecto
    path('index/', index)
]
