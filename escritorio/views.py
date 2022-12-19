from rest_framework.viewsets import ModelViewSet
from escritorio.models import Custos
from escritorio.serializers import CustosSerializer

# Create your views here.

class ProcessosViewSet(ModelViewSet):
    queryset = Custos.objects.all()
    serializer_class = CustosSerializer
    permission_classes = []
