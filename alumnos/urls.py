from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlumnoViewSet

router = DefaultRouter()
router.register(r'alumnos', AlumnoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
