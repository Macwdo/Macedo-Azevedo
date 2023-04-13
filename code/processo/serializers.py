from advogado.models import Advogado
from cliente.models import Cliente, ParteADV
from cliente.serializers import ClienteSerializer, ParteADVSerializer
from advogado.serializer import AdvogadoSerializer
from rest_framework import serializers
from .models import *


class ProcessosAssuntosSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("assunto")
        model = ProcessosAssuntos

class ProcessosHonorariosSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id", "referente",
            "valor", "processo",
            "advogado_responsavel"
            )
        model = ProcessosHonorarios


class ProcessosAnexosSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ProcessosAnexos


class ProcessosSerializer(serializers.ModelSerializer):


    cliente = ClienteSerializer(many=False, required=False)

    cliente_de = AdvogadoSerializer(many=False, required=False)

    parte_adversa = ParteADVSerializer(many=False, required=False)

    advogado_responsavel = AdvogadoSerializer(many=False, required=False)

    colaborador = AdvogadoSerializer(many=False, required=False)

    cliente_id = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all(), write_only=True)
    parte_adversa_id = serializers.PrimaryKeyRelatedField(queryset=ParteADV.objects.all(), write_only=True)
    cliente_de_id = serializers.PrimaryKeyRelatedField(queryset=Advogado.objects.all(), write_only=True)
    advogado_responsavel_id = serializers.PrimaryKeyRelatedField(queryset=Advogado.objects.all(), write_only=True)
    colaborador_id = serializers.PrimaryKeyRelatedField(queryset=Advogado.objects.all(), write_only=True, required=False)

    honorarios_registrados = ProcessosHonorariosSerializer(many=True, read_only=True)
    anexos_registrados = ProcessosAnexosSerializer(many=True, read_only=True)

    class Meta:
        model = Processos
        fields = (
            "id","codigo_processo","posicao",
            "assunto", "observacoes",
            "municipio", "estado", "n_vara","vara","rastreado",
            "iniciado","finalizado", "honorarios",
            "advogado_responsavel","cliente",
            "cliente_de","colaborador","parte_adversa","cliente",
            "honorarios_registrados", "anexos_registrados","cliente_id",
            "parte_adversa_id","cliente_de_id","advogado_responsavel_id","colaborador_id"
            
        )


    def create(self, validated_data):
        validated_data["cliente"] = validated_data.pop("cliente_id")
        validated_data["parte_adversa"] = validated_data.pop("parte_adversa_id")
        validated_data["cliente_de"] = validated_data.pop("cliente_de_id")
        validated_data["advogado_responsavel"] = validated_data.pop("advogado_responsavel_id")
        if validated_data.get("colaborador_id"):
            validated_data["colaborador"] = validated_data.pop("colaborador_id")
        processo = Processos.objects.create(**validated_data)

        return processo