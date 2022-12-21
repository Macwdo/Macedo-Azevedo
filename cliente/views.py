from rest_framework.viewsets import ModelViewSet
from .models import ParteADV
from .models import Cliente 
from .serializers import ClienteSerializer, ParteADVSerializer
from rest_framework.permissions import IsAuthenticated


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        fields = {}
        for k, v in self.request.query_params.items():
            fields[k + "__icontains"] = v
        qs = Cliente.objects.filter(**fields)
        return qs


class ParteADVViewSet(ModelViewSet):
    queryset = ParteADV.objects.all()
    serializer_class = ParteADVSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        fields = {}
        for k, v in self.request.query_params.items():
            fields[k + "__icontains"] = v
        qs = ParteADV.objects.filter(**fields)
        return qs

