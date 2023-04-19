from cliente.serializers import ClienteSerializer, ParteADVSerializer
from advogado.serializer import AdvogadoSerializer
from rest_framework import serializers
from processo.models import Processos, ProcessosAnexos, ProcessosHonorarios, ProcessosAssuntos


class ProcessosAssuntosSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("assunto")
        model = ProcessosAssuntos


class ProcessosHonorariosSerializer(serializers.ModelSerializer):
    advogado_responsavel = AdvogadoSerializer(many=False, read_only=True)
    advogado_responsavel_id = serializers.IntegerField()

    class Meta:
        fields = (
            "id", "referente",
            "valor", "processo",
            "advogado_responsavel", "advogado_responsavel_id",
            "ganho"
        )
        model = ProcessosHonorarios
        read_only_fields = ("processo",)


class ProcessosAnexosSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id", "nome_do_anexo",
            "arquivo", "created_at",
            "processo"
        )
        model = ProcessosAnexos
        read_only_fields = ("processo",)


class ProcessosSerializer(serializers.ModelSerializer):

    cliente = ClienteSerializer(many=False, required=False)

    cliente_de = AdvogadoSerializer(many=False, required=False)

    parte_adversa = ParteADVSerializer(many=False, required=False)

    advogado_responsavel = AdvogadoSerializer(many=False, required=False)

    colaborador = AdvogadoSerializer(many=False, required=False)

    cliente_id = serializers.IntegerField(write_only=True)
    parte_adversa_id = serializers.IntegerField(write_only=True)
    cliente_de_id = serializers.IntegerField(write_only=True)
    advogado_responsavel_id = serializers.IntegerField(write_only=True)
    colaborador_id = serializers.IntegerField(write_only=True, required=False)

    honorarios_registrados = ProcessosHonorariosSerializer(
        many=True, read_only=True)
    anexos_registrados = ProcessosAnexosSerializer(many=True, read_only=True)

    class Meta:
        model = Processos
        fields = (
            "id", "codigo_processo", "posicao",
            "assunto", "observacoes",
            "municipio", "estado", "n_vara", "vara", "rastreado",
            "iniciado", "finalizado", "honorarios",
            "advogado_responsavel", "cliente",
            "cliente_de", "colaborador", "parte_adversa", "cliente",
            "honorarios_registrados", "anexos_registrados",
            "cliente_id", "parte_adversa_id", "cliente_de_id",
            "advogado_responsavel_id", "colaborador_id"

        )
