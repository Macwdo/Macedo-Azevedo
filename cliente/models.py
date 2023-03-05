from django.db import models


class Cliente(models.Model):

    choice_tipo =(("PF", "Pessoa Fisica"), ("PJ", "Pessoa Juridica"))

    nome = models.CharField(max_length=100, blank=False, null=False, default="Não informado")
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



class ParteADV(models.Model):

    choice_tipo =[("PF", "Pessoa Fisica"), ("PJ", "Pessoa Juridica")]

    nome = models.CharField(max_length=50, blank=False, null=False, default="Não informado")
    email = models.CharField(max_length=50, blank=False, null=False, default="Não informado")
    numero = models.CharField(max_length=20, blank=False, null=False, default="Não informado")
    cpf_cnpj = models.CharField(max_length=30, default="Não informado")
    registro = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(choices=choice_tipo, max_length=2)

    def __str__(self) -> str:
        return f"{self.nome}"

    class Meta:
        verbose_name_plural = 'Parte ADV'

class ContaCliente(models.Model):
    registro = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pix = models.CharField(max_length=150, blank=False, null=False, default="Não informado")
    agencia = models.CharField(max_length=150, blank=False, null=False, default="Não informado")
    conta = models.CharField(max_length=150, blank=False, null=False, default="Não informado")

class ContaParteAdv(models.Model):
    registro = models.ForeignKey(ParteADV, on_delete=models.CASCADE)
    pix = models.CharField(max_length=150, blank=False, null=False, default="Não informado")
    agencia = models.CharField(max_length=150, blank=False, null=False, default="Não informado")
    conta = models.CharField(max_length=150, blank=False, null=False, default="Não informado")