from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from advogado.models import Advogado


class AdvogadoSerializer(ModelSerializer):
    class Meta:
        model = Advogado
        fields = "__all__"

class AdvogadoCurrentSerializer(Serializer):
    honorarios = serializers.FloatField()
    nome = serializers.CharField()
    processos = serializers.IntegerField()
    email = serializers.CharField()

    
    