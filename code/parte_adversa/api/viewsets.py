from django.db.models import Q
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from parte_adversa.models import ParteAdv, ParteAdvEndereco
from .serializers import ParteAdvSerializer, ParteAdvEnderecoSerializer


class ParteAdvViewSet(ModelViewSet):
    queryset = ParteAdv.objects.all()
    serializer_class = ParteAdvSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        q = self.request.query_params.get("q", None)
        tipo = self.request.query_params.get("tipo", None)

        adverse_part_qs = ParteAdv.objects.all()

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

class ParteAdvEnderecoViewSet(ModelViewSet):
    queryset = ParteAdvEndereco.objects.all()
    serializer_class = ParteAdvEnderecoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        parteadv_pk = int(self.kwargs.get("parteadv_pk"))
        try:
            parteadv = ParteAdv.objects.get(pk=parteadv_pk)
        except ParteAdv.DoesNotExist:
            raise NotFound()
        return self.queryset.filter(pk=parteadv_pk)
