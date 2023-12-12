from django.contrib import admin

from registry.models import (
    Registry,
    RegistryAddress,
    RegistryCnpj,
    RegistryContact,
    RegistryCpf,
)

# Register your models here.


@admin.register(Registry)
class RegistryAdmin(admin.ModelAdmin):
    ...


@admin.register(RegistryContact)
class RegistryContactAdmin(admin.ModelAdmin):
    ...


@admin.register(RegistryAddress)
class RegistryAddressAdmin(admin.ModelAdmin):
    ...


@admin.register(RegistryCpf)
class RegistryCpfAdmin(admin.ModelAdmin):
    ...


@admin.register(RegistryCnpj)
class RegistryCnpjAdmin(admin.ModelAdmin):
    ...
