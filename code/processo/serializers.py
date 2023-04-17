from advogado.models import Advogado
from cliente.models import Cliente, ParteADV
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
    advogado_responsavel_pk = serializers.PrimaryKeyRelatedField(queryset=Advogado.objects.all(), write_only=True)

    class Meta:
        fields = (
            "id", "referente",
            "valor", "processo",
            "advogado_responsavel", "advogado_responsavel_pk",
            "ganho"
            )
        model = ProcessosHonorarios
        read_only_fields = ("processo",)

    def create(self, validated_data):
        validated_data["advogado_responsavel"] = validated_data.pop("advogado_responsavel_pk")
        processo_honorario = ProcessosHonorarios.objects.create(**validated_data)
        return processo_honorario
    
    def update(self, instance, validated_data):
        validated_data["advogado_responsavel"] = validated_data.pop("advogado_responsavel_pk")
        return super().update(instance, validated_data)


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

    cliente_pk = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all(), write_only=True)
    parte_adversa_pk = serializers.PrimaryKeyRelatedField(queryset=ParteADV.objects.all(), write_only=True)
    cliente_de_pk = serializers.PrimaryKeyRelatedField(queryset=Advogado.objects.all(), write_only=True)
    advogado_responsavel_pk = serializers.PrimaryKeyRelatedField(queryset=Advogado.objects.all(), write_only=True)
    colaborador_pk = serializers.PrimaryKeyRelatedField(queryset=Advogado.objects.all(), write_only=True, required=False)
    
    honorarios_registrados = ProcessosHonorariosSerializer(many=True, read_only=True)
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
            "honorarios_registrados", "anexos_registrados", "cliente_pk",
            "parte_adversa_pk", "cliente_de_pk", "advogado_responsavel_pk", "colaborador_pk"
            
        )


    def create(self, validated_data):
        validated_data["cliente"] = validated_data.pop("cliente_pk")
        validated_data["parte_adversa"] = validated_data.pop("parte_adversa_pk")
        validated_data["cliente_de"] = validated_data.pop("cliente_de_pk")
        validated_data["advogado_responsavel"] = validated_data.pop("advogado_responsavel_pk")
        if validated_data.get("colaborador_id"):
            validated_data["colaborador"] = validated_data.pop("colaborador_pk")
        processo = Processos.objects.create(**validated_data)
        return processo
    
    def update(self, instance, validated_data):
        validated_data["cliente"] = validated_data.pop("cliente_pk")
        validated_data["parte_adversa"] = validated_data.pop("parte_adversa_pk")
        validated_data["cliente_de"] = validated_data.pop("cliente_de_pk")
        validated_data["advogado_responsavel"] = validated_data.pop("advogado_responsavel_pk")
        if validated_data.get("colaborador_pk"):
            validated_data["colaborador"] = validated_data.pop("colaborador_pk")
        return super().update(instance, validated_data)
