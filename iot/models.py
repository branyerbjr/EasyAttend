from django.db import models

class IoT(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    topic = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    lugar = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
