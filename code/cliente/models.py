from django.db import models


class Cliente(models.Model):
    choice_tipo = (
        ("PF", "Pessoa Fisica"), ("PJ", "Pessoa Juridica")
    )
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cpf_cnpj = models.CharField(max_length=30, blank=False)
    tipo = models.CharField(choices=choice_tipo, max_length=2)
    endereco = models.TextField(default="Não Informado")

    def __str__(self) -> str:
        return f"{self.nome}"

    class Meta:
        verbose_name_plural = 'Cliente'


class ClienteEndereco(models.Model):
    cliente = models.ForeignKey(Cliente, models.CASCADE)
    endereco = models.CharField(
        max_length=255, null=False, blank=False, default="Não Identificado")
    complemento = models.CharField(
        max_length=255, null=False, blank=False, default="Não Identificado")
    cep = models.CharField(max_length=255, null=False,
                           blank=False, default="Não Identificado")


