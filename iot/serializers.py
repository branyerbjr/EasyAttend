from rest_framework import serializers
from .models import IoT

class IoTSerializer(serializers.ModelSerializer):
    class Meta:
        model = IoT
        fields = ['id', 'nombre', 'descripcion', 'topic', 'fecha_registro', 'lugar']
