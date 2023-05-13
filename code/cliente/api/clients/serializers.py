from rest_framework import serializers
from cliente.models import Cliente, ClienteEndereco


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"


class ClienteEnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteEndereco
        fields = "__all__"
