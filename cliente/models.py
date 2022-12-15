from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self) -> str:
        return f"{self.nome}"
    
    class Meta:
        verbose_name_plural = 'Cliente'


class ClientePF(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self) -> str:
        return f"{self.cliente.nome}"

    class Meta:
        verbose_name_plural = 'Cliente PF'
    

class ClientePJ(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=18, unique=True)

    def __str__(self) -> str:
        return f"{self.cliente.nome}"

    class Meta:
        verbose_name_plural = 'Cliente PJ'


class ParteADV(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self) -> str:
        return f"{self.nome}"

    class Meta:
        verbose_name_plural = 'Parte ADV'


class ParteADVPF(models.Model):
    parteadv = models.ForeignKey(ParteADV, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self) -> str:
        return f"{self.parteadv.nome}"

    class Meta:
        verbose_name_plural = 'Parte ADV PF'

    

class ParteADVPJ(models.Model):
    parteadv = models.ForeignKey(ParteADV, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=18, unique=True)

    def __str__(self) -> str:
        return f"{self.parteadv.nome}"

    class Meta:
        verbose_name_plural = 'Parte ADV PJ'

