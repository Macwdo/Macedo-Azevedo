from django.contrib import admin

from .models import Processos, ProcessosHonorarios, ProcessosAnexos


@admin.register(Processos)
class Processos_admin(admin.ModelAdmin):
    ...

@admin.register(ProcessosHonorarios)
class ProcessosHonorarios_admin(admin.ModelAdmin):
    ...

@admin.register(ProcessosAnexos)
class ProcessosAnexos_admin(admin.ModelAdmin):
    ...
