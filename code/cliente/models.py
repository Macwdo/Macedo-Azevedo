from django.db import models


class Cliente(models.Model):
    choice_tipo =(("PF", "Pessoa Fisica"), ("PJ", "Pessoa Juridica"))
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=False, null=False, default="Não informado")
    numero = models.CharField(max_length=20, blank=False, null=False, default="Não informado")
    registro = models.DateTimeField(auto_now_add=True)
    endereco = models.CharField(max_length=200, blank=False, null=False, default="Não informado")
    cpf_cnpj = models.CharField(max_length=30, default="Não informado")
    tipo = models.CharField(choices=choice_tipo, max_length=2)

    def __str__(self) -> str:
        return f"{self.nome}"
    
    class Meta:
        verbose_name_plural = 'Cliente'


class ClienteEndereco(models.Model):
    cliente = models.ForeignKey(Cliente, models.CASCADE)
    endereco = models.CharField(max_length=255, null=False, blank=False, default="Não Identificado")
    complemento = models.CharField(max_length=255, null=False, blank=False, default="Não Identificado")
    cep = models.CharField(max_length=255, null=False, blank=False, default="Não Identificado")


class ParteADV(models.Model):
    choice_tipo = [("PF", "Pessoa Fisica"), ("PJ", "Pessoa Juridica")]
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=False, null=False, default="Não informado")
    numero = models.CharField(max_length=20, blank=False, null=False, default="Não informado")
    endereco = models.CharField(max_length=200, blank=False, null=False, default="Não informado")
    cpf_cnpj = models.CharField(max_length=30, default="Não informado")
    registro = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(choices=choice_tipo, max_length=2)

    def __str__(self) -> str:
        return f"{self.nome}"

    class Meta:
        verbose_name_plural = 'Parte ADV'

class ParteADVEndereco(models.Model):
    parte_adv = models.ForeignKey(ParteADV, models.CASCADE)
    endereco = models.CharField(max_length=255, null=False, blank=False, default="Não Identificado")
    complemento = models.CharField(max_length=255, null=False, blank=False, default="Não Identificado")
    cep = models.CharField(max_length=30, null=False, blank=False, default="Não Identificado")