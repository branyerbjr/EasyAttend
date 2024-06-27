from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import Asistencia
from alumnos.models import Alumno
from .serializers import AsistenciaSerializer
from alumnos.serializers import AlumnoSerializer
import requests

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

@api_view(['POST'])
def registrar_asistencia(request):
    dni = request.data.get('dni')
    id_dispositivo = request.data.get('id_dispositivo')
    
    if not dni or not id_dispositivo:
        return Response({'error': 'DNI e ID de dispositivo son requeridos'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        alumno = Alumno.objects.get(dni=dni)
    except Alumno.DoesNotExist:
        # Realizar solicitud a la API externa para obtener datos de alumno
        url = f"https://api.apis.net.pe/v2/reniec/dni?numero={dni}"
        headers = {
            'Authorization': 'Bearer apis-token-9226.FxawTl9Rx8rYWTrxDTksCHHvFeQ324Qd'
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            nombre = data['nombres']
            apellidos = f"{data['apellidoPaterno']} {data['apellidoMaterno']}"
            
            # Crear nuevo alumno
            alumno = Alumno.objects.create(
                nombre=nombre,
                apellidos=apellidos,
                dni=dni,
                codigo_estudiante=dni  # Ajustar según necesidades
            )
        else:
            return Response({'error': 'No se pudo obtener los datos del alumno'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Crear registro de asistencia
    asistencia = Asistencia.objects.create(
        alumno=alumno,
        lugar=id_dispositivo  # Aquí se guarda el id_dispositivo como lugar
    )
    
    return Response({'mensaje': 'Asistencia registrada exitosamente'}, status=status.HTTP_201_CREATED)


class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def list_asistencias(self, request):
        queryset = Asistencia.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)