from django.db import models

from advogado.models import Advogado

# Create your models here.

class Receita(models.Model):
    nome_ganho = models.CharField(max_length=40)
    valor_ganho = models.FloatField()
    gerado = models.DateTimeField()
    pago = models.BooleanField(default=True)
    responsavel = models.ForeignKey(Advogado, on_delete=models.SET_NULL, null=True)


    def __str__(self) -> str:
        return f"{self.nome_ganho} R${self.valor_ganho}"

class Custos(models.Model):
    nome_custo = models.CharField(max_length=40)
    valor_custo = models.FloatField()
    gerado = models.DateTimeField()
    pago = models.BooleanField(default=False)
    responsavel = models.ForeignKey(Advogado, on_delete=models.SET_NULL, null=True)


    def __str__(self) -> str:
        return f"{self.nome_custo} R${self.valor_custo}"

    class Meta:
        verbose_name_plural = 'Custos'