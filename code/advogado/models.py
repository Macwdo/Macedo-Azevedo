from django.contrib.auth.models import User
from django.db import models


class Advogado(models.Model):

    def upload_file_name(self, filename):
        return f'images/{filename}'

    nome = models.CharField(max_length=40, blank=False)
    email = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    oab = models.CharField(max_length=8, unique=True, null=False, blank=True)
    image = models.ImageField(upload_to="images/", default=None, null=True)

    def __str__(self) -> str:
        return f"{self.nome}"

    class Meta:
        verbose_name_plural = 'Advogado'