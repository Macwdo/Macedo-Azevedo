from django.conf import settings
from django.db import models


class Advogado(models.Model):
    name = models.CharField(max_length=255, blank=False, null=True)
    email = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, null=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='lawyer_user',
    )
    oab = models.CharField(max_length=12, null=False, blank=False)
    image = models.ImageField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return f'{self.name}'

    @property
    def revenue(self):
        from processo.models import ProcessosHonorarios

        return sum(
            [
                (
                    lawsuit_value.valor
                    if lawsuit_value.ganho
                    else (lawsuit_value.valor * -1)
                )
                for lawsuit_value in ProcessosHonorarios.objects.filter(
                    advogado_responsavel=self
                )
            ]
        )

    class Meta:
        verbose_name_plural = 'Advogado'
