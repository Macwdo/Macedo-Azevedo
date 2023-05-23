from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from parte_adversa.api.viewsets import AdversePartAddressViewSet, AdversePartViewSet
from django.urls import path
from parte_adversa.views import adverse_part_list, adverse_part_create, adverse_part_delete, adverse_part_detail, adverse_part_edit
from parte_adversa.views import adverse_part_address_create, adverse_part_address_delete, adverse_part_address_edit
from parte_adversa.views import adverse_part_contact_create, adverse_part_contact_delete, adverse_part_contact_edit

app_name = "adverse_part"


parteadv_router = SimpleRouter()
parteadv_router.register(r'parteadv', AdversePartViewSet)

parteadv_router_nested = NestedSimpleRouter(
    parteadv_router,
    r'parteadv',
    lookup='parteadv'
)
parteadv_router_nested.register(
    r'endereco',
    AdversePartAddressViewSet,
    basename='parteadv-endereco'
)

urlpatterns = [
    path("", adverse_part_list , name="adverse_part_list"),
    path("create", adverse_part_create, name="adverse_part_create"),
    path("<int:adverse_part_id>", adverse_part_detail, name="adverse_part_detail"),
    path("<int:adverse_part_id>/edit", adverse_part_edit, name="adverse_part_edit"),
    path("<int:adverse_part_id>/delete", adverse_part_delete , name="adverse_part_delete"),

    path("<int:adverse_part_id>/contact/create", adverse_part_contact_create, name="adverse_part_contact_create"),
    path("<int:adverse_part_id>/contact/<int:contact_id>/edit", adverse_part_contact_edit, name="adverse_part_contact_edit"),
    path("<int:adverse_part_id>/contact/<int:contact_id>/delete", adverse_part_contact_delete, name="adverse_part_contact_delete"),

    path("<int:adverse_part_id>/address/create", adverse_part_address_create, name="adverse_part_address_create"),
    path("<int:adverse_part_id>/address/<int:address_id>/edit", adverse_part_address_edit, name="adverse_part_address_edit"),
    path("<int:adverse_part_id>/address/<int:address_id>/delete", adverse_part_address_delete , name="adverse_part_address_delete"),
]