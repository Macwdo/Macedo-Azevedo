from django.contrib import admin
from .models import ParteADV, ParteADVPF, ParteADVPJ, Cliente, ClientePF, ClientePJ
# Register your models here.

@admin.register(Cliente)
class Clientes_admin(admin.ModelAdmin):
    ...

@admin.register(ClientePF)
class Clientes_admin(admin.ModelAdmin):
    ...

@admin.register(ClientePJ)
class Clientes_admin(admin.ModelAdmin):
    ...



@admin.register(ParteADV)
class ParteADV_admin(admin.ModelAdmin):
    ...

@admin.register(ParteADVPF)
class ParteADVPF_admin(admin.ModelAdmin):
    ...

@admin.register(ParteADVPJ)
class ParteADVPJ_admin(admin.ModelAdmin):
    ...

