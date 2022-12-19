from rest_framework.viewsets import ModelViewSet
from .models import ParteADV
from .models import Cliente 
from .serializers import ClienteSerializer, ParteADVSerializer


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


    def get_queryset(self):
        queryparams = self.request.query_params
        queryset = Cliente.objects.all()
        pf, pj = queryparams.get("pf", False), queryparams.get("pj", False)
        if pj:
            queryset = Cliente.objects.filter(tipo="PJ")
        elif pf:
            queryset = Cliente.objects.filter(tipo="PF")
        return queryset



class ParteADVViewSet(ModelViewSet):
    queryset = ParteADV.objects.all()
    serializer_class = ParteADVSerializer


    def get_queryset(self):
        queryparams = self.request.query_params
        queryset = ParteADV.objects.all()
        pf, pj = queryparams.get("pf", False), queryparams.get("pj", False)
        if pj:
            queryset = ParteADV.objects.filter(tipo="PJ")
        elif pf:
            queryset = ParteADV.objects.filter(tipo="PF")
        return queryset

