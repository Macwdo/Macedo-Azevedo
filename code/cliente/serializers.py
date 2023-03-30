from rest_framework import serializers
from .models import ParteADV, Cliente, ParteADVEndereco, ClienteEndereco


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = "__all__"


class ClienteEnderecoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClienteEndereco
        fields = "__all__"


class ParteADVEnderecoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParteADVEndereco
        fields = "__all__"


class ParteADVSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParteADV
        fields = "__all__"
