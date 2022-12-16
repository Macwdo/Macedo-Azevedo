from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import now

from advogado.models import Advogado
from cliente.models import Cliente, ParteADV

# Create your models here.

class Processos(models.Model):

    posicao_choice = [("Autor","Autor"),("Réu","Réu")]

    assunto_choices = [
        ("Trabalhista", "Direito Trabalhista"),
        ("Previdenciário", "Direito Previdenciário"),
        ("Civil", "Direito Civil")
    ]

    codigo_processo = models.CharField(max_length=25)
    advogado_responsavel = models.ForeignKey(Advogado, on_delete=models.SET_NULL, null=True, related_name="advogado_responsavel")
    parte_adversa = models.ForeignKey(ParteADV, on_delete=models.SET_NULL, null=True, related_name="parte_adversa")
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, related_name="clientes")
    posicao = models.CharField(max_length=5, choices=posicao_choice)
    colaborador = models.ForeignKey(Advogado, on_delete=models.SET_NULL, null=True, blank=True, related_name="colaborador")
    assunto = models.CharField(choices=assunto_choices, max_length=15)
    observacoes = models.CharField(max_length=255, default="Sem observações", null=True, blank=True)
    honorarios = models.FloatField(blank=True, default=0)
    municipio = models.CharField(max_length=35)
    estado = models.CharField(max_length=2)
    n_vara = models.CharField(max_length=10)
    vara = models.CharField(max_length=50)
    iniciado = models.DateField(default=now)
    finalizado = models.DateTimeField(blank=True, null=True)
    arquivos = models.ManyToManyField('ProcessosArquivos', blank=True)


    def __str__(self) -> str:
        return f"{self.cliente.nome} X {self.parte_adversa.nome} - {self.codigo_processo}"

    class Meta:
        verbose_name_plural = 'Processos'



def dir_files_processo(instance, file):
    return f"{instance.processo}-cod={instance.processo.codigo_processo}/{file}"


class ProcessosArquivos(models.Model):
    processo = models.ForeignKey(Processos, on_delete=models.CASCADE)
    arquivos = models.FileField(upload_to=dir_files_processo)

    def __str__(self) -> str:
        return f"{self.pk} {self.arquivos}"

    class Meta:
        verbose_name_plural = 'Processos Arquivos'
