from rest_framework import serializers
from .models import ParteADV, Cliente


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = "__all__"



class ParteADVSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParteADV
        fields = "__all__"
