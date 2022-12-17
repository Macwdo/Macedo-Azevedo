from rest_framework.viewsets import ModelViewSet
from .models import Cliente
from .serializers import ClienteSerializer
# Create your views here.

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

