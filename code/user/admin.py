from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MAUser

admin.site.register(MAUser, UserAdmin)
