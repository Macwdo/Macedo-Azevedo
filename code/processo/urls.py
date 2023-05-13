from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from processo.api.viewsets import ProcessosViewSet, ProcessosHonorariosViewSet, ProcessosAnexosViewSet, ProcessosMovimentoViewSet
from django.urls import path
from .views import list

app_name = "lawsuits"

processo_router = SimpleRouter()
processo_router.register(r'processo', ProcessosViewSet)

processo_router_nested = NestedSimpleRouter(
    processo_router,
    r'processo',
    lookup='processo'
)
processo_router_nested.register(
    r'honorario',
    ProcessosHonorariosViewSet,
    basename='processo-honorario'
)
processo_router_nested.register(
    r'anexo',
    ProcessosAnexosViewSet,
    basename='processo-anexo'
)

processo_router_nested.register(
    r'movimento',
    ProcessosMovimentoViewSet,
    basename='processo-movimento'
)


urlpatterns = [
    path("", list, name="list")
]