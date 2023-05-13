from django.db.models import Q
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from cliente.models import Cliente, ClienteEndereco
from .serializers import ClienteSerializer, ClienteEnderecoSerializer


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        q = self.request.query_params.get("q", None)
        tipo = self.request.query_params.get("tipo", None)

        client_qs = Cliente.objects.all()

        if q:
            client_qs = client_qs.filter(
                Q(nome__icontains=q) |
                Q(email__icontains=q) |
                Q(numero__icontains=q) |
                Q(cpf_cnpj__icontains=q) |
                Q(endereco__icontains=q) 
            )

        if tipo:
            client_qs = client_qs.filter(tipo=tipo)

        return client_qs.order_by("-id")

class ClienteEnderecoViewSet(ModelViewSet):
    queryset = ClienteEndereco.objects.all()
    serializer_class = ClienteEnderecoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cliente_pk = int(self.kwargs.get("cliente_pk"))
        try:
            cliente = Cliente.objects.get(pk=cliente_pk)
        except Cliente.DoesNotExist:
            raise NotFound()
        return self.queryset.filter(pk=cliente_pk)


