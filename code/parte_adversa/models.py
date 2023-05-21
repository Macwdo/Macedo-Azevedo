from django.db import models


class ParteAdv(models.Model):
    choice_tipo = (
        ("PF", "Pessoa Fisica"), ("PJ", "Pessoa Juridica")
    )
    nome = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cpf_cnpj = models.CharField(max_length=30, blank=False)
    tipo = models.CharField(choices=choice_tipo, max_length=2)
    imagem = models.ImageField()

    def __str__(self) -> str:
        return f"{self.nome} {self.cpf_cnpj}"

    class Meta:
        verbose_name_plural = 'Parte Adversa'


class ParteAdvEndereco(models.Model):
    parte_adv = models.ForeignKey(ParteAdv, models.CASCADE, related_name="adverse_part_adress")
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=50) 
    complemento = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.parte_adv} - {self.endereco} - {self.cep}"

    class Meta:
        verbose_name_plural = 'Endereços da Parte Adversa'

class ParteAdvContato(models.Model):
    parte_adv = models.ForeignKey(ParteAdv, models.CASCADE, related_name="adverse_part_contact")
    email = models.CharField(max_length=255, null=True, blank=False)
    numero = models.CharField(max_length=20,  null=True, blank=False)

    def __str__(self) -> str:
        return f"{self.parte_adv} - {self.email} - {self.numero}"

    class Meta:
        verbose_name_plural = 'Contatos Parte Adversa'
    



