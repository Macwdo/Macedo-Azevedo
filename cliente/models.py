import datetime

from django.db import models

# Create your models here.

class Cliente(models.Model):

    choice_tipo =(("PF", "Pessoa Fisica"), ("PJ", "Pessoa Juridica"))

    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    registro = models.DateTimeField(auto_now=True)
    cpf_cnpj = models.CharField(max_length=30)
    tipo = models.CharField(choices=choice_tipo, max_length=2)


    def __str__(self) -> str:
        return f"{self.nome}"
    
    class Meta:
        verbose_name_plural = 'Cliente'



class ParteADV(models.Model):

    choice_tipo =[("PF", "Pessoa Fisica"), ("PJ", "Pessoa Juridica")]

    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    cpf_cnpj = models.CharField(max_length=30)
    registro = models.DateTimeField(auto_now=True)
    tipo = models.CharField(choices=choice_tipo, max_length=2)

    def __str__(self) -> str:
        return f"{self.nome}"

    class Meta:
        verbose_name_plural = 'Parte ADV'



