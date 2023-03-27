from django.contrib import admin
from escritorio.models import Custos
# Register your models here.

@admin.register(Custos)
class CustosAdmin(admin.ModelAdmin):
    ...