from django.db.models import Q
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from cliente.models import ParteADV, ParteADVEndereco
from .serializers import ParteADVSerializer, ParteADVEnderecoSerializer


class ParteADVViewSet(ModelViewSet):
    queryset = ParteADV.objects.all()
    serializer_class = ParteADVSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        q = self.request.query_params.get("q", None)
        tipo = self.request.query_params.get("tipo", None)

        adverse_part_qs = ParteADV.objects.all()

        if q:
            adverse_part_qs = adverse_part_qs.filter(
                Q(nome__icontains=q) |
                Q(email__icontains=q) |
                Q(numero__icontains=q) |
                Q(cpf_cnpj__icontains=q) |
                Q(endereco__icontains=q) 
            )

        if tipo:
            adverse_part_qs = adverse_part_qs.filter(tipo=tipo)

        return adverse_part_qs.order_by("-id")

class ParteADVEnderecoViewSet(ModelViewSet):
    queryset = ParteADVEndereco.objects.all()
    serializer_class = ParteADVEnderecoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        parteadv_pk = int(self.kwargs.get("parteadv_pk"))
        try:
            parteadv = ParteADV.objects.get(pk=parteadv_pk)
        except ParteADV.DoesNotExist:
            raise NotFound()
        return self.queryset.filter(pk=parteadv_pk)
