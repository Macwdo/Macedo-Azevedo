from django.urls import path
from rest_framework_nested.routers import NestedSimpleRouter, SimpleRouter

from processo.api.viewsets import (
    ProcessosAnexosViewSet,
    ProcessosHonorariosViewSet,
    ProcessosMovimentoViewSet,
    ProcessosViewSet,
)

from .views import (
    lawsuit_board,
    lawsuit_create,
    lawsuit_delete,
    lawsuit_detail,
    lawsuit_edit,
    lawsuit_file_create,
    lawsuit_file_delete,
    lawsuit_file_edit,
    lawsuit_finalize,
    lawsuit_list,
    lawsuit_revert_state,
    lawsuit_value_create,
    lawsuit_value_delete,
    lawsuit_value_edit,
)

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

    path("board", lawsuit_board, name="lawsuit_board"),
    path("create", lawsuit_create, name="lawsuit_create"),
    path("", lawsuit_list, name="lawsuit_list"),
    path("<int:lawsuit_id>", lawsuit_detail, name="lawsuit_detail"),
    path("<int:lawsuit_id>/edit", lawsuit_edit , name="lawsuit_edit"),
    path("<int:lawsuit_id>/delete", lawsuit_delete , name="lawsuit_delete"),
    path("<int:lawsuit_id>/finalize", lawsuit_finalize, name="lawsuit_finalize" ),
    path("<int:lawsuit_id>/revert-state", lawsuit_revert_state, name="lawsuit_revert_state" ),
    
    path("<int:lawsuit_id>/values/create", lawsuit_value_create, name="lawsuit_value_create"),
    path("<int:lawsuit_id>/values/<int:lawsuit_value_id>/edit", lawsuit_value_edit , name="lawsuit_value_edit"),
    path("<int:lawsuit_id>/values/<int:lawsuit_value_id>/delete", lawsuit_value_delete , name="lawsuit_value_delete"),
    
    path("<int:lawsuit_id>/file/create", lawsuit_file_create, name="lawsuit_file_create"),
    path("<int:lawsuit_id>/file/<int:lawsuit_file_id>/edit", lawsuit_file_edit , name="lawsuit_file_edit"),
    path("<int:lawsuit_id>/file/<int:lawsuit_file_id>/delete", lawsuit_file_delete , name="lawsuit_file_delete"),
  
    
]