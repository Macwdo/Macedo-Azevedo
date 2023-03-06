from django.urls import include, path
from rest_framework import routers

from .views import *

app_name = "processo"

router = routers.SimpleRouter()

router.register(r'processo', ProcessosViewSet)
router.register(r'honorario', ProcessoHonorariosViewSet)

urlpatterns = [
    path("processosws/", tjRjScraping, name="processoWebScraping"),
] + router.urls
