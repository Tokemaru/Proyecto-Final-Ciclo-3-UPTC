from pyexpat import model
from django.db import models


# aca creamos la conexion con todas las diferentes tablas de la base de datos por medio de clases asi:
class libros (models.Model):
    ID_Libro = models.CharField(max_length=40, primary_key=True) # aca indicamos la llave primaria que ayuda a la conexion con las otras tablas
    Nombre_Libro = models.CharField(max_length=80) #charfield indica el tipo de dato que la tabla va a recibir y la extension del texto
    Autor = models.CharField(max_length=80) #
    Estado = models.CharField(max_length=40)


class prestamos (models.Model):
    ID_Libro = models.CharField (max_length=40, primary_key=True)
    ID_User = models.CharField (max_length=20)
    Estado = models.CharField (max_length=20)
    Fecha_inicio = models.DateField ()
    Fecha_fin = models.DateField ()

class usuarios (models.Model):
    ID_User = models.CharField (max_length=20, primary_key=True)
    Nombre_Usuario = models.CharField (max_length=40)
    Direccion_Usuario = models.CharField (max_length=60)





