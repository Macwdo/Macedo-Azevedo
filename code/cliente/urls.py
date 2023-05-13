from django.urls import path
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from cliente.api.clients.viewsets import ClienteEnderecoViewSet, ClienteViewSet
from cliente.api.adverse_parts.viewsets import ParteADVViewSet, ParteADVEnderecoViewSet

app_name = "registros"

cliente_router = SimpleRouter()
cliente_router.register(r'cliente', ClienteViewSet)

cliente_router_nested = NestedSimpleRouter(
    cliente_router,
    r'cliente',
    lookup='cliente'
)

cliente_router_nested.register(
    r'endereco',
    ClienteEnderecoViewSet,
    basename='cliente-endereco'
)

parteadv_router = SimpleRouter()
parteadv_router.register(r'parteadv', ParteADVViewSet)

parteadv_router_nested = NestedSimpleRouter(
    parteadv_router,
    r'parteadv',
    lookup='parteadv'
)
parteadv_router_nested.register(
    r'endereco',
    ParteADVEnderecoViewSet,
    basename='parteadv-endereco'
)


urlpatterns = []
