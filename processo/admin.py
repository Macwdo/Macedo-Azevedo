from django.contrib import admin

from .models import Processos


@admin.register(Processos)
class Processos_admin(admin.ModelAdmin):
    ...

