from rest_framework import serializers
from parte_adversa.models import ParteAdv, ParteAdvEndereco


class ParteAdvEnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParteAdvEndereco
        fields = "__all__"


class ParteAdvSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParteAdv
        fields = "__all__"
