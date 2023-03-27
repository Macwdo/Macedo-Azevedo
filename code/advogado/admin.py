from django.contrib import admin

from .models import Advogado

# Register your models here.

@admin.register(Advogado)
class Advogado_admin(admin.ModelAdmin):
    ...