from django.shortcuts import render
from django.views import View
from django.db.models import Q
from api.models import libros

def index(request):
    return render(render, 'index.html')
# Creamos la clase que va a mostrar los datos solicitados de la base de datos
def comunicacionDB (request):
    busqueda= request.get.get('consulta')
    libros= libros.objects.all()

    if busqueda:
        libros = libros.objects.filter(
            Q(Nombre_Libro_icontains = busqueda) |
            Q(Autor_icontains = busqueda) 
        ).distinct()
    return render(request, 'resultado.html')


