from advogado.models import Advogado
from cliente.models import Cliente, ParteADV
from cliente.serializers import ClienteSerializer, ParteADVSerializer
from rest_framework import serializers
from processo.utils import get_current_time
from .models import *
from .views import *


class ProcessosAssuntosSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("assunto")
        model = ProcessosAssuntos

class ProcessosHonorariosSerializer(serializers.ModelSerializer):
    advogado_responsavel = serializers.StringRelatedField(source="responsavel")
    responsavel = serializers.PrimaryKeyRelatedField(queryset=Advogado.objects.all(), write_only=True)

    codigo_processo = serializers.StringRelatedField(source="processo")
    processo = serializers.PrimaryKeyRelatedField(queryset=Processos.objects.all(), write_only=True)

    class Meta:
        fields = (
            "id", "referente", "codigo_processo",
            "valor", "processo",
            "responsavel", "advogado_responsavel"
            )
        model = ProcessosHonorarios


class ProcessosAnexosSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ProcessosAnexos


class ProcessosSerializer(serializers.ModelSerializer):

    finalizar = serializers.BooleanField(default=False, write_only=True, required=False)
    nome_cliente = serializers.StringRelatedField(source="cliente", read_only=True)
    cliente_de_dr = serializers.StringRelatedField(source="cliente_de", read_only=True)
    nome_parte = serializers.StringRelatedField(source="parte_adversa", read_only=True)
    advogado = serializers.StringRelatedField(source="advogado_responsavel", read_only=True)
    advogado_colaborador = serializers.StringRelatedField(source="colaborador", read_only=True)

    cliente = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all(), write_only=True)
    parte_adversa = serializers.PrimaryKeyRelatedField(queryset=ParteADV.objects.all(), write_only=True)

    cliente_de = serializers.PrimaryKeyRelatedField(queryset=Advogado.objects.all(), write_only=True)
    advogado_responsavel = serializers.PrimaryKeyRelatedField(queryset=Advogado.objects.all(), write_only=True)
    colaborador = serializers.PrimaryKeyRelatedField(queryset=Advogado.objects.all(), write_only=True, required=False)

    honorarios_registrados = ProcessosHonorariosSerializer(many=True, read_only=True)
    anexos_registrados = ProcessosAnexosSerializer(many=True, read_only=True)

    class Meta:
        model = Processos
        fields = (
            "id", "advogado","cliente","cliente_de_dr","cliente_de",
            "nome_cliente", "nome_parte", "advogado_colaborador",
            "codigo_processo","advogado_responsavel", "parte_adversa",
            "cliente","posicao","colaborador",
            "assunto", "observacoes",
            "municipio", "estado", "n_vara","vara",
            "iniciado","finalizado","finalizar", "honorarios",
            "honorarios_registrados", "anexos_registrados"
            )
        

    def create(self, validated_data):
        validated_data.pop("finalizar")
        processo = Processos.objects.create(**validated_data)
        return processo
    
    def update(self, instance, validated_data):
        validated_data.get("finalizar", None)
        if validated_data.get("finalizar", False) and instance.finalizado is None:
            validated_data["finalizado"] = get_current_time()
                    
        return super().update(instance, validated_data)
        