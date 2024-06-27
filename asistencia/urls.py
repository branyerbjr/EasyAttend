from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AsistenciaViewSet, registrar_asistencia

router = DefaultRouter()
router.register(r'asistencia', AsistenciaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('registrar-asistencia/', registrar_asistencia, name='registrar_asistencia'),
]
