from django.urls import path
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from cliente.api.clients.viewsets import ClienteEnderecoViewSet, ClienteViewSet
from cliente.views import list, detail, delete

app_name = "client"

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


urlpatterns = [
    path("", list, name="list"),
    path("<int:pk>", detail, name="detail"),
    path("<int:pk>/delete", delete , name="delete")
]