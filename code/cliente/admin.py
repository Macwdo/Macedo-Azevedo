from django.contrib import admin
from cliente.models import Cliente, ClienteContato, ClienteEndereco
# Register your models here.
    
@admin.register(Cliente)
class ParteAdvAdmin(admin.ModelAdmin):
    ...

@admin.register(ClienteContato)
class ParteAdvContato(admin.ModelAdmin):
    ...

@admin.register(ClienteEndereco)
class ParteAdvEnderecoAdmin(admin.ModelAdmin):
    ...