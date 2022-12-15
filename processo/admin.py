from django.contrib import admin
from .models import Processos, ProcessosArquivos

@admin.register(Processos)
class Processos_admin(admin.ModelAdmin):
    ...

@admin.register(ProcessosArquivos)
class Processos_admin_arquivos(admin.ModelAdmin):
    ...