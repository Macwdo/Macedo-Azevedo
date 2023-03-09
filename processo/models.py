from advogado.models import Advogado
from cliente.models import Cliente, ParteADV
from django.db import models


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

    codigo_processo = models.CharField(max_length=25, unique=True, null=False, blank=False)
    advogado_responsavel = models.ForeignKey(Advogado, on_delete=models.SET_NULL, null=True, related_name="advogado_responsavel", default="Não Informado")
    parte_adversa = models.ForeignKey(ParteADV, on_delete=models.SET_NULL, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, related_name="clientes")
    cliente_de = models.ForeignKey(Advogado, on_delete=models.SET_NULL, null= True, blank=False)
    posicao = models.CharField(choices=posicao_choice, max_length=5)
    colaborador = models.ForeignKey(Advogado, on_delete=models.SET_NULL, null=True, blank=True, related_name="colaborador")
    assunto = models.CharField(choices=assunto_choices, max_length=15)
    observacoes = models.CharField(max_length=255, default="Sem observações", null=True, blank=True)
    municipio = models.CharField(max_length=40)
    estado = models.CharField(max_length=20)
    n_vara = models.CharField(max_length=30)
    vara = models.CharField(max_length=50)
    iniciado = models.DateTimeField(auto_now_add=True)
    finalizado = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    def honorarios_registrados(self):
        return ProcessosHonorarios.objects.filter(processo=Processos.objects.get(pk=self.pk))

    def honorarios(self):
        honorarios = ProcessosHonorarios.objects.filter(processo=Processos.objects.get(pk=self.pk))
        total = 0
        for i in honorarios:
            total += i.valor
        return total
        

    def __str__(self) -> str:
        return f"{self.codigo_processo}"

    class Meta:
        verbose_name_plural = 'Processos'


class ProcessosHonorarios(models.Model):
    referente = models.CharField(max_length=255)
    processo = models.ForeignKey(Processos, models.CASCADE, null=False, blank=False)
    responsavel = models.ForeignKey(Advogado, models.SET_NULL, null=True, blank=False)
    valor = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProcessosAnexos(models.Model):
    processo = models.ForeignKey(Processos, models.CASCADE, null=False, blank=False)
    arquivo = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

