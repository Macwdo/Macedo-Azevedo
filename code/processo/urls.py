from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from processo.views import ProcessosViewSet, ProcessosHonorariosViewSet, ProcessosAnexosViewSet


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
    basename='processo-honorario'
)

urlpatterns = [
] + router.urls + processo_routers.urls
