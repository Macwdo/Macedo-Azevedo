from rest_framework import serializers
from .models import ParteADV, Cliente


class ClienteSerializer(serializers.ModelSerializer):
    cpf = serializers.CharField(default=None, write_only=True, required=False)
    cnpj = serializers.CharField(default=None, write_only=True, required=False)

    class Meta:
        model = Cliente
        fields = "__all__"



class ParteADVSerializer(serializers.ModelSerializer):
    cpf = serializers.CharField(default=None, write_only=True, required=False)
    cnpj = serializers.CharField(default=None, write_only=True, required=False)

    class Meta:
        model = ParteADV
        fields = "__all__"

