from rest_framework import routers
from django.urls import path
from .views import sofHonorarios, sofProcessos


app_name = "escritorio"

router = routers.SimpleRouter()


urlpatterns = [
    path('honorarios/', sofHonorarios),
    path('processos/', sofProcessos)
]
