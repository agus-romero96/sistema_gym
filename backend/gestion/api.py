from rest_framework.viewsets import ModelViewSet
from .models import Cliente,Instructor,Clase
from .serializers import ClienteSerializer,InstructorSerializer,ClaseSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()  # Consulta para obtener todos los clientes
    serializer_class = ClienteSerializer

class InstructorViewSet(ModelViewSet):
    queryset = Instructor.objects.all()  # Consulta para obtener todos los instructores
    serializer_class = InstructorSerializer

class ClaseViewSet(ModelViewSet):
    queryset = Clase.objects.all()  # Consulta para obtener todas las clases
    serializer_class = ClaseSerializer