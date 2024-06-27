from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IoTViewSet

router = DefaultRouter()
router.register(r'dispositivos', IoTViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
