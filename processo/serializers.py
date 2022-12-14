from rest_framework import serializers
from .models import Processos, ProcessosArquivos
from cliente.serializers import ClienteSerializer, ParteADVSerializer
from advogado.models import Advogado
from cliente.models import Cliente, ParteADV
from processo.utils import get_current_time


class ProcessosArquivosSerializer(serializers.ModelSerializer):
    
    nome_processo = serializers.StringRelatedField(source="processo", read_only=True)
    processo = serializers.PrimaryKeyRelatedField(queryset=Processos.objects.all(), write_only=True)

    class Meta:
        model = ProcessosArquivos
        fields = ("id", "processo", "nome_processo", "arquivo")

class ProcessosSerializer(serializers.ModelSerializer):

    finalizar = serializers.BooleanField(default=False, write_only=True, required=False)
    nome_cliente = serializers.StringRelatedField(source="cliente", read_only=True)
    nome_parte = serializers.StringRelatedField(source="parte_adversa", read_only=True)
    advogado = serializers.StringRelatedField(source="advogado_responsavel", read_only=True)
    advogado_colaborador = serializers.StringRelatedField(source="colaborador", read_only=True)

    cliente = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all(), write_only=True)
    parte_adversa = serializers.PrimaryKeyRelatedField(queryset=ParteADV.objects.all(), write_only=True)


    advogado_responsavel = serializers.PrimaryKeyRelatedField(queryset=Advogado.objects.all(), write_only=True)
    colaborador = serializers.PrimaryKeyRelatedField(queryset=Advogado.objects.all(), write_only=True, required=False)



    processos = ProcessosArquivosSerializer(many=True, read_only=True)
    uploaded_arquivos = serializers.ListField(
        child=serializers.FileField(),
        write_only=True,
        required=False

    )

    class Meta:
        model = Processos
        fields = (
            "id", "uploaded_arquivos", "advogado","cliente",
            "nome_cliente", "nome_parte", "advogado_colaborador",
            "codigo_processo","advogado_responsavel", "parte_adversa",
            "cliente","posicao","colaborador",
            "assunto", "observacoes", "honorarios",
            "municipio", "estado", "n_vara",
            "vara","iniciado","finalizado","finalizar",
            "processos"
        )

    def create(self, validated_data):
        validated_data.pop("finalizar")
        if validated_data.get("uploaded_arquivos"):
            uploaded_arquivos = validated_data.pop("uploaded_arquivos")
            processo = Processos.objects.create(**validated_data)
            for arquivo in uploaded_arquivos:
                processo_arquivo_new = ProcessosArquivos.objects.create(processo=processo, arquivo=arquivo)
            return processo
        processo = Processos.objects.create(**validated_data)
        return processo
    
    def update(self, instance, validated_data):
        validated_data.get("finalizar", None)
        if validated_data and instance.finalizado is None:
            validated_data["finalizado"] = get_current_time()
            advogado_responsavel = Advogado.objects.get(pk=instance.advogado_responsavel.id)
            advogado_responsavel.honorarios += instance.honorarios
            advogado_responsavel.save()

        return super().update(instance, validated_data)
        