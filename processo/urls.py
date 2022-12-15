from django.urls import path
from .views import criarprocesso


app_name = "processo"

urlpatterns = [
    path("criar/", criarprocesso, name="Criando")
]



