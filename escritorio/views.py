from rest_framework.viewsets import ModelViewSet
from escritorio.models import Custos
from escritorio.serializers import CustosSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CustosViewSet(ModelViewSet):
    queryset = Custos.objects.all()
    serializer_class = CustosSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        fields = {}
        for k, v in self.request.query_params.items():
            fields[k + "__icontains"] = v
        qs = Custos.objects.filter(**fields)
        return qs
