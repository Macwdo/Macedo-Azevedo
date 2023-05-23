from django.db import models


class AdversePart(models.Model):
    choice_tipo = (
        ("PF", "Pessoa Fisica"), ("PJ", "Pessoa Juridica")
    )
    nome = models.CharField(max_length=100)
    cpf_cnpj = models.CharField(max_length=30, blank=False)
    estado_civil = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100)
    tipo = models.CharField(choices=choice_tipo, max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nome}"

    class Meta:
        verbose_name_plural = 'Parte Adversa'


class AdversePartAddress(models.Model):
    parte_adv = models.ForeignKey(AdversePart, models.CASCADE, related_name="adverse_part_address")
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=50) 
    complemento = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.endereco}, Nº{self.numero}, {self.cep}"

    class Meta:
        verbose_name_plural = 'Endereços da Parte Adversa'

class AdversePartContact(models.Model):
    parte_adv = models.ForeignKey(AdversePart, models.CASCADE, related_name="adverse_part_contact")
    email = models.CharField(max_length=255, null=True, blank=False)
    numero = models.CharField(max_length=20,  null=True, blank=False)

    def __str__(self) -> str:
        return f"{self.parte_adv} - {self.email} - {self.numero}"

    class Meta:
        verbose_name_plural = 'Contatos Parte Adversa'
    



