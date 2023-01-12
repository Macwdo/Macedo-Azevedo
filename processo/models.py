from django.core.exceptions import ValidationError
from django.db import models
import datetime

from advogado.models import Advogado
from cliente.models import Cliente, ParteADV

# Create your models here.


def dir_files_processo(instance, file):
    return f"{instance.processo}/{file}"


class Processos(models.Model):
    
    assunto_choices = [
        ("Trabalhista", "Direito Trabalhista"),
        ("Previdenciário", "Direito Previdenciário"),
        ("Civil", "Direito Civil")
    ]

    posicao_choice = [
        ("Autor", "Autor"),
        ("Réu", "Réu")
    ]

    codigo_processo = models.CharField(max_length=25, unique=True)
    advogado_responsavel = models.ForeignKey(Advogado, on_delete=models.SET_NULL, null=True, related_name="advogado_responsavel", default="Não Informado")
    parte_adversa = models.ForeignKey(ParteADV, on_delete=models.SET_NULL, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, related_name="clientes")
    posicao = models.CharField(choices=posicao_choice, max_length=5)
    colaborador = models.ForeignKey(Advogado, on_delete=models.SET_NULL, null=True, blank=True, related_name="colaborador")
    assunto = models.CharField(choices=assunto_choices, max_length=15)
    observacoes = models.CharField(max_length=255, default="Sem observações", null=True, blank=True)
    honorarios = models.FloatField(blank=True, default=0)
    municipio = models.CharField(max_length=35)
    estado = models.CharField(max_length=2)
    n_vara = models.CharField(max_length=10)
    vara = models.CharField(max_length=50)
    iniciado = models.DateField(default=datetime.date.today)
    finalizado = models.DateTimeField(blank=True, null=True)
    arquivos = models.FileField(upload_to=dir_files_processo, default="", blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.cliente.nome} X {self.parte_adversa.nome} - {self.codigo_processo}"


    class Meta:
        verbose_name_plural = 'Processos'



class ProcessosArquivos(models.Model):
    processo = models.ForeignKey(Processos, on_delete=models.CASCADE, related_name="processos")
    arquivo = models.FileField(upload_to=dir_files_processo, default="", blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.pk} {self.arquivo}"

    class Meta:
        verbose_name_plural = 'Processos Arquivos'
