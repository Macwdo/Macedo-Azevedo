from django.db import models

# Create your models here.

class Advogado(models.Model):
    nome = models.CharField(max_length=40, blank=False)
    honorarios = models.FloatField(blank=True, default=0)
    email = models.CharField(max_length=50)
    image = models.ImageField()

    def __str__(self) -> str:
        return f"{self.nome}"

    class Meta:
        verbose_name_plural = 'Advogado'