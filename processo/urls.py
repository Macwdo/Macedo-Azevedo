from django.urls import include, path
from rest_framework import routers
from .views import processoWebScraping

from .views import ProcessosViewSet

app_name = "processo"

router = routers.SimpleRouter()

router.register(r'processo', ProcessosViewSet)


urlpatterns = [
    path("processosws/", processoWebScraping, name="processoWebScraping")
]
