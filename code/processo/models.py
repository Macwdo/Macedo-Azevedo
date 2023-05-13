from advogado.models import Advogado
from cliente.models import Cliente, ParteADV
from django.db import models
from datetime import datetime


class ProcessosAssuntos(models.Model):
    assunto = models.CharField(max_length=255)


class Processos(models.Model):
    posicao_choice = [
        ("autor", "Autor"),
        ("reu", "Réu")
    ]
    codigo_processo = models.CharField(max_length=25, null=False, blank=False)
    advogado_responsavel = models.ForeignKey(Advogado, on_delete=models.SET_NULL, null=True, blank=False, related_name="advogado_responsavel")
    parte_adversa = models.ForeignKey(ParteADV, on_delete=models.SET_NULL, null=True, blank=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=False, related_name="cliente")
    cliente_de = models.ForeignKey(Advogado, on_delete=models.SET_NULL, null=True, blank=False)
    posicao = models.CharField(choices=posicao_choice, max_length=5)
    colaborador = models.ForeignKey(Advogado, on_delete=models.SET_NULL, null=True, blank=True, related_name="colaborador")
    observacoes = models.CharField(max_length=255, default="Sem observações", null=True, blank=True)
    estado = models.TextField()
    municipio = models.TextField()
    assunto = models.CharField(max_length=255)
    n_vara = models.CharField(max_length=30)
    vara = models.CharField(max_length=50)
    iniciado = models.DateTimeField(auto_now_add=True)
    finalizado = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def honorarios_registrados(self):
        return ProcessosHonorarios.objects.filter(processo=Processos.objects.get(pk=self.pk))

    @property
    def honorarios(self):
        honorarios = ProcessosHonorarios.objects.filter(
            processo=Processos.objects.get(pk=self.pk))
        total = 0
        for i in honorarios:
            total += i.valor if i.ganho else (i.valor * -1)
        return total

    def anexos_registrados(self):
        return ProcessosAnexos.objects.filter(processo=Processos.objects.get(pk=self.pk)).order_by("-id")

    @property
    def tracked(self):
        rastreaveis = ["8.19"]
        if self.codigo_processo[16:20] in rastreaveis:
            return True
        return False

    def __str__(self) -> str:
        return f"{self.codigo_processo}"

    @property
    def track_history(self):
        return ProcessosMovimento.objects.filter(processo_id=self.pk)

    class Meta:
        verbose_name_plural = 'Processos'


class ProcessosMovimento(models.Model):
    processo = models.ForeignKey(
        Processos, models.CASCADE, null=False, blank=False)
    tipo_movimento = models.CharField(
        max_length=255, null=False, default="Vazio")
    last_date = models.CharField(max_length=10, null=False, blank=False)
    data = models.TextField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def date(self):
        return datetime(int(self.last_date[6:]), int(self.last_date[3:5]), int(self.last_date[0:2]))

    def __str__(self):
        return f"{self.processo} {self.tipo_movimento}"


class ProcessosHonorarios(models.Model):
    referente = models.CharField(max_length=255,)
    processo = models.ForeignKey(
        Processos, models.CASCADE, null=False, blank=False)
    advogado_responsavel = models.ForeignKey(
        Advogado, models.SET_NULL, null=True, blank=False)
    valor = models.FloatField()
    ganho = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.processo} {self.valor}"


class ProcessosAnexos(models.Model):
    nome_do_anexo = models.CharField(max_length=100, null=False, blank=False)
    processo = models.ForeignKey(
        Processos, models.CASCADE, null=False, blank=False)
    arquivo = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)

    def size(self):
        return self.arquivo.size
    
    # def type(self):


    def __str__(self) -> str:
        return f"{self.processo} {self.nome_do_anexo}"
