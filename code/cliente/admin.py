from django.contrib import admin
from cliente.models import ParteADV, Cliente
# Register your models here.
    
@admin.register(Cliente)
class Clientes_admin(admin.ModelAdmin):
    ...

@admin.register(ParteADV)
class ParteADV_admin(admin.ModelAdmin):
    ...
