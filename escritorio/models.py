from django.db import models

# Create your models here.

class Custos(models.Model):
    nome_custo = models.CharField(max_length=40)
    detalhes = models.CharField(max_length=200)
    custo = models.FloatField()
    prazo = models.DateField()
    pago = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.nome_custo} R${self.custo}"

    class Meta:
        verbose_name_plural = 'Custos'