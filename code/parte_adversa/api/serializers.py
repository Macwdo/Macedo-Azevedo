from rest_framework import serializers
from parte_adversa.models import ParteADV, ParteADVEndereco


class ParteADVEnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParteADVEndereco
        fields = "__all__"


class ParteADVSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParteADV
        fields = "__all__"
