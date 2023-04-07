from advogado.models import Advogado
from cliente.models import Cliente, ParteADV
from django.db import models


class ProcessosAssuntos(models.Model):
    assunto = models.CharField(max_length=255)


class Processos(models.Model):
    posicao_choice = [
        ("Autor", "Autor"),
        ("Réu", "Réu")
    ]

    codigo_processo = models.CharField(max_length=25, unique=True, null=False, blank=False)
    advogado_responsavel = models.ForeignKey(Advogado, on_delete=models.SET_NULL, null=True, related_name="advogado_responsavel", default="Não Informado")
    parte_adversa = models.ForeignKey(ParteADV, on_delete=models.SET_NULL, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, related_name="cliente")
    cliente_de = models.ForeignKey(Advogado, on_delete=models.SET_NULL, null=True, blank=False)
    posicao = models.CharField(choices=posicao_choice, max_length=5)
    colaborador = models.ForeignKey(Advogado, on_delete=models.SET_NULL, null=True, blank=True, related_name="colaborador")
    observacoes = models.CharField(max_length=255, default="Sem observações", null=True, blank=True)
    municipio = models.CharField(max_length=40)
    assunto = models.CharField(max_length=255)
    estado = models.CharField(max_length=20)
    n_vara = models.CharField(max_length=30)
    vara = models.CharField(max_length=50)
    iniciado = models.DateTimeField(auto_now_add=True)
    finalizado = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def honorarios_registrados(self):
        return ProcessosHonorarios.objects.filter(processo=Processos.objects.get(pk=self.pk))

    def honorarios(self):
        honorarios = ProcessosHonorarios.objects.filter(processo=Processos.objects.get(pk=self.pk))
        total = 0
        for i in honorarios:
            total += i.valor
        return total

    def anexos_registrados(self):
        return ProcessosAnexos.objects.filter(processo=Processos.objects.get(pk=self.pk))


    def __str__(self) -> str:
        return f"{self.codigo_processo}"

    class Meta:
        verbose_name_plural = 'Processos'


class ProcessosHonorarios(models.Model):

    referente_field = [
        ("Honorarios", "Honorarios"),
        ("Custo", "Custo"),
        ("Taxas", "Taxas")
                       ]

    referente = models.CharField(max_length=255,)
    processo = models.ForeignKey(Processos, models.CASCADE, null=False, blank=False)
    responsavel = models.ForeignKey(Advogado, models.SET_NULL, null=True, blank=False)
    valor = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.processo} {self.valor}"



class ProcessosAnexos(models.Model):
    nome_do_anexo = models.CharField(max_length=100, null=False, blank=False)
    processo = models.ForeignKey(Processos, models.CASCADE, null=False, blank=False)
    arquivo = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.processo} {self.nome_do_anexo}"

