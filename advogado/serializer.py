from rest_framework.serializers import ModelSerializer
from .models import Advogado


class AdvogadoSerializer(ModelSerializer):
    class Meta:
        model = Advogado
        fields = "__all__"