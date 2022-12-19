from rest_framework.viewsets import ModelViewSet
from escritorio.models import Custos
from escritorio.serializers import CustosSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CustosViewSet(ModelViewSet):
    queryset = Custos.objects.all()
    serializer_class = CustosSerializer
    permission_classes = [IsAuthenticated]
