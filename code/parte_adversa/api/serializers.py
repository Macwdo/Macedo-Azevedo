from rest_framework import serializers
from parte_adversa.models import AdversePart, AdversePartAddress


class AdversePartAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdversePartAddress
        fields = "__all__"


class AdversePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdversePart
        fields = "__all__"
