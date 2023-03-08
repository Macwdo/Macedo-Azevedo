from django.urls import include, path
from rest_framework import routers

from .views import *

app_name = "processo"

router = routers.SimpleRouter()

router.register(r'processo', ProcessosViewSet)
router.register(r'processo-honorario', ProcessosHonorariosViewSet)
router.register(r'processo-anexos', ProcessosAnexosViewSet)

urlpatterns = [
    path("processosws/", tjRjScraping, name="processoWebScraping"),
] + router.urls
