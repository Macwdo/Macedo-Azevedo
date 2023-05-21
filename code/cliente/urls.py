from django.urls import path
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from cliente.api.clients.viewsets import ClienteEnderecoViewSet, ClienteViewSet
from cliente.views import client_list, client_create, client_delete, client_detail, client_edit
from cliente.views import client_address_create, client_address_delete, client_address_edit
from cliente.views import client_contact_create, client_contact_delete, client_contact_edit

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
    path("", client_list , name="client_list"),
    path("create", client_create, name="client_create"),
    path("<int:client_id>", client_detail, name="client_detail"),
    path("<int:client_id>/edit", client_edit, name="client_edit"),
    path("<int:client_id>/delete", client_delete , name="client_delete"),

    path("<int:client_id>/contact/create", client_contact_create, name="client_contact_create"),
    path("<int:client_id>/contact/<int:contact_id>/edit", client_contact_edit, name="client_contact_edit"),
    path("<int:client_id>/contact/<int:contact_id>/delete", client_contact_delete, name="client_contact_delete"),

    path("<int:client_id>/address/create", client_address_create, name="client_address_create"),
    path("<int:client_id>/address/<int:address_id>/edit", client_address_edit, name="client_address_edit"),
    path("<int:client_id>/address/<int:address_id>/delete", client_address_delete , name="client_address_delete"),
]