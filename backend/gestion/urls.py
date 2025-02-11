from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ClienteViewSet, InstructorViewSet, ClaseViewSet


router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'instructores', InstructorViewSet, basename='instructor')
router.register(r'clases', ClaseViewSet, basename='clase')

urlpatterns = [
    path('', include(router.urls)),  # Incluye todas las rutas generadas por el router
]
