from django.contrib import admin
from cliente.models import Cliente, ClienteContato, ClienteEndereco
# Register your models here.
    
@admin.register(Cliente)
class AdversePartAdmin(admin.ModelAdmin):
    ...

@admin.register(ClienteContato)
class AdversePartContact(admin.ModelAdmin):
    ...

@admin.register(ClienteEndereco)
class AdversePartAddressAdmin(admin.ModelAdmin):
    ...