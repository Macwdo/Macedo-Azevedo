from django.urls import path
from .views import ClienteViewSet, ParteADVViewSet, ParteADVEnderecoViewSet, ClienteEnderecoViewSet, sendEmail, task_test
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter


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


urlpatterns = [
    path("send-email/", sendEmail, name="reset"),
    path("testing/", task_test, name="reset")
] + parteadv_router.urls + parteadv_router_nested.urls + cliente_router.urls + cliente_router_nested.urls

