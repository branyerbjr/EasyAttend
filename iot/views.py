from rest_framework import viewsets
from .models import IoT
from .serializers import IoTSerializer

class IoTViewSet(viewsets.ModelViewSet):
    queryset = IoT.objects.all()
    serializer_class = IoTSerializer
