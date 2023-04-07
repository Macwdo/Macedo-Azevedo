from django.urls import include, path
from rest_framework import routers
from rest_framework_nested import routers as nrouters
from .views import *


app_name = "processos"


router = nrouters.SimpleRouter()
router.register(r'processo', ProcessosViewSet)

processo_routers = nrouters.NestedSimpleRouter(
    router,
    r'processo',
    lookup='processo'
)

processo_routers.register(
    r'honorario',
    ProcessosHonorariosViewSet,
    basename='processo-honorario'
)

processo_routers.register(
    r'anexo',
    ProcessosAnexosViewSet,
    basename='processo-honorario'
)

urlpatterns = [
    path("processosws/", tjRjScraping, name="processoWebScraping"),
    path("processo/<int:id>/finalizar/", finalizar_processo, name="finalizar")
] + router.urls + processo_routers.urls
