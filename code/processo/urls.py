from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from processo.views import ProcessosViewSet, ProcessosHonorariosViewSet, ProcessosAnexosViewSet, ProcessosMovimentoViewSet


app_name = "processos"


router = SimpleRouter()
router.register(r'processo', ProcessosViewSet)

processo_routers = NestedSimpleRouter(
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
    basename='processo-anexo'
)

processo_routers.register(
    r'movimento',
    ProcessosMovimentoViewSet,
    basename='processo-movimento'
)


urlpatterns = [
] + router.urls + processo_routers.urls
