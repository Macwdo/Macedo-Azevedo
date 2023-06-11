from user.models import MAUser
from django.db import models
from django.conf import settings

class Advogado(models.Model):
    name = models.CharField(max_length=255, blank=False, null=True)
    email = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="user")
    oab = models.CharField(max_length=12, unique=True, null=False, blank=True)
    image = models.ImageField(default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.name}"

    @property
    def revenue(self):
        return sum([gain.profit for gain in self.lawyer.all()])

    class Meta:
        verbose_name_plural = 'Advogado'
        
        
