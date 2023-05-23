from django.db.models import Q
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from parte_adversa.models import AdversePart, AdversePartAddress
from .serializers import AdversePartSerializer, AdversePartAddressSerializer


class AdversePartViewSet(ModelViewSet):
    queryset = AdversePart.objects.all()
    serializer_class = AdversePartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        q = self.request.query_params.get("q", None)
        tipo = self.request.query_params.get("tipo", None)

        adverse_part_qs = AdversePart.objects.all()

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

class AdversePartAddressViewSet(ModelViewSet):
    queryset = AdversePartAddress.objects.all()
    serializer_class = AdversePartAddressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        parteadv_pk = int(self.kwargs.get("parteadv_pk"))
        try:
            parteadv = AdversePart.objects.get(pk=parteadv_pk)
        except AdversePart.DoesNotExist:
            raise NotFound()
        return self.queryset.filter(pk=parteadv_pk)
