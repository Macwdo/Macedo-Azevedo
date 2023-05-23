from django.contrib import admin
from parte_adversa.models import AdversePart, AdversePartContact, AdversePartAddress
# Register your models here.

@admin.register(AdversePart)
class AdversePartAdmin(admin.ModelAdmin):
    ...

@admin.register(AdversePartContact)
class AdversePartContact(admin.ModelAdmin):
    ...

@admin.register(AdversePartAddress)
class AdversePartAddressAdmin(admin.ModelAdmin):
    ...
