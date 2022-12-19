from rest_framework import serializers
from escritorio.models import Custos

class CustosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custos
        fields = "__all__"
