from django.contrib import admin
from cliente.models import Cliente
# Register your models here.
    
@admin.register(Cliente)
class Clientes_admin(admin.ModelAdmin):
    ...

