from django.contrib import admin
from .models import ArquivoModels
# Register your models here.

@admin.register(ArquivoModels)
class ArquivoModels(admin.ModelAdmin):
    ...