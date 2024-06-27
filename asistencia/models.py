from django.db import models
from alumnos.models import Alumno

class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    lugar = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.alumno} - {self.lugar} - {self.fecha_hora}"
