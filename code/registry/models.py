from django.db import models
from advogado.models import Advogado


class Registry(models.Model):
    name = models.CharField(max_length=100)
    civil_state = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, null=True)
    client_of = models.ForeignKey(Advogado, on_delete=models.SET_NULL, null=True, blank=False, related_name="client_of")
    

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'Registro'
        
    @property
    def is_client(self) -> bool:
        return self.client.exists()
    
    @property
    def is_adverse_part(self) -> bool:
        return self.adverse_part.exists()
    
    @property
    def is_indicator(self) -> bool:
        return self.indicated_by.exists()
        

class RegistryCpf(models.Model):
    registry = models.OneToOneField(Registry, on_delete=models.CASCADE, primary_key=True, related_name="cpf")
    cpf = models.CharField(max_length=14)

    def __str__(self) -> str:
        return self.cpf

    
class RegistryCnpj(models.Model):
    registry = models.OneToOneField(Registry, on_delete=models.CASCADE, primary_key=True, related_name="cnpj")
    cnpj = models.CharField(max_length=18)

    def __str__(self) -> str:
        return self.cnpj


class RegistryAddress(models.Model):
    registry = models.ForeignKey(Registry, models.CASCADE, related_name="registry_address")
    address = models.CharField(max_length=255)
    address_number = models.CharField(max_length=50) 
    complement = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)
    reference = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.address}, Nº{self.address_number}, {self.cep}"

    class Meta:
        verbose_name_plural = 'Endereço dos registros'

class RegistryContact(models.Model):
    registry = models.ForeignKey(Registry, models.CASCADE, related_name="registry_contact")
    email = models.CharField(max_length=255, null=True, blank=False)
    phone_number = models.CharField(max_length=20,  null=True, blank=False)

    def __str__(self) -> str:
        return f"{self.email}, {self.phone_number}"

    class Meta:
        verbose_name_plural = 'Contato do registro'
    



