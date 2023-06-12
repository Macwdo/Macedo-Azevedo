from advogado.models import Advogado
from django.db import models
from datetime import datetime
from registry.models import Registry


class ProcessosAssuntos(models.Model):
    assunto = models.CharField(max_length=255)


class Processos(models.Model):
    posicao_choice = [
        ("autor", "Autor"),
        ("reu", "Réu")
    ]
    codigo_processo = models.CharField(max_length=25, null=False, blank=False)
    advogado_responsavel = models.ForeignKey(Advogado, on_delete=models.PROTECT, null=True, blank=False, related_name="lawsuit_lawyer")
    parte_adversa = models.ForeignKey(Registry, on_delete=models.PROTECT, null=True, blank=False, related_name="lawsuit_adverse_part")
    cliente = models.ForeignKey(Registry, on_delete=models.PROTECT, null=True, blank=False, related_name="lawsuit_client")
    posicao = models.CharField(choices=posicao_choice, max_length=5)
    colaborador = models.ForeignKey(Advogado, on_delete=models.PROTECT, null=True, blank=True, related_name="lawsuit_colaborator")
    assunto = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    vara = models.CharField(max_length=50)
    observacoes = models.TextField()
    iniciado = models.DateTimeField()
    finalizado = models.DateTimeField(blank=True, null=True)
    indicado_por = models.ForeignKey(Registry, on_delete=models.SET_NULL, null=True, blank=True, related_name="lawsuit_indicated_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def honorarios_registrados(self):
        return ProcessosHonorarios.objects.filter(processo=Processos.objects.get(pk=self.pk))


    @property
    def profit(self):
        honorarios = ProcessosHonorarios.objects.filter(
            processo=Processos.objects.get(pk=self.pk))
        total = 0
        for honorario in honorarios:
            total += honorario.valor if honorario.ganho else (honorario.valor * -1)
        return float(f"{total:.3f}")
    
    @property
    def gain(self):
        honorarios = ProcessosHonorarios.objects.filter(
            processo=Processos.objects.get(pk=self.pk))
        total = 0
        for honorario in honorarios:
            if honorario.ganho:
                total += honorario.valor
        return float(f"{total:.3f}")
    
    @property
    def cost(self):
        honorarios = ProcessosHonorarios.objects.filter(
            processo=Processos.objects.get(pk=self.pk))
        total = 0
        for honorario in honorarios:
            if not honorario.ganho:
                total += honorario.valor
        return float(f"{total:.3f}")

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
    processo = models.ForeignKey(Processos, models.CASCADE, null=False, blank=False)
    tipo_movimento = models.CharField(max_length=255, null=False, default="Vazio")
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
    processo = models.ForeignKey(Processos, models.CASCADE, null=False, blank=False, related_name="lawsuit_values")
    advogado_responsavel = models.ForeignKey(Advogado, models.SET_NULL, null=True, blank=False, related_name="lawsuit_values_lawyer")
    valor = models.FloatField()
    ganho = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{'+' if self.ganho else '-' }R${self.valor}"


class ProcessosAnexos(models.Model):
    nome_do_anexo = models.CharField(max_length=100, null=False, blank=False)
    processo = models.ForeignKey(Processos, models.CASCADE, null=False, blank=False, related_name="lawsuit_files")
    arquivo = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def size(self):
        return self.arquivo.size
    
    def __str__(self) -> str:
        return f"{self.processo} {self.nome_do_anexo}"
