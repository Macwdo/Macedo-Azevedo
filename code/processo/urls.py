from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from processo.api.viewsets import ProcessosViewSet, ProcessosHonorariosViewSet, ProcessosAnexosViewSet, ProcessosMovimentoViewSet
from django.urls import path
from .views import lawsuit_list, lawsuit_detail, lawsuit_delete, lawsuit_create, lawsuit_edit

app_name = "lawsuit"

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
    path("create", lawsuit_create, name="lawsuit_create"),
    path("", lawsuit_list, name="lawsuit_list"),
    path("<int:pk>", lawsuit_detail, name="lawsuit_detail"),
    path("<int:pk>/delete", lawsuit_delete , name="lawsuit_delete"),
    path("<int:pk>/edit", lawsuit_edit , name="lawsuit_edit")
]