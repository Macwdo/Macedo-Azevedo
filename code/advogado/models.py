from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Advogado(models.Model):
    nome = models.CharField(max_length=40, blank=False)
    honorarios = models.FloatField(blank=True, default=0)
    email = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.nome}"

    class Meta:
        verbose_name_plural = 'Advogado'