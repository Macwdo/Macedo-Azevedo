from django.contrib import admin
from parte_adversa.models import ParteAdv, ParteAdvContato, ParteAdvEndereco
# Register your models here.

@admin.register(ParteAdv)
class ParteAdvAdmin(admin.ModelAdmin):
    ...

@admin.register(ParteAdvContato)
class ParteAdvContato(admin.ModelAdmin):
    ...

@admin.register(ParteAdvEndereco)
class ParteAdvEnderecoAdmin(admin.ModelAdmin):
    ...
