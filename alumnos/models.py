from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    codigo_estudiante = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
