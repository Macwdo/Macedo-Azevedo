from django.urls import path

from registry.views import (
    registry_address_create,
    registry_address_delete,
    registry_address_edit,
    registry_contact_create,
    registry_contact_delete,
    registry_contact_edit,
    registry_create,
    registry_delete,
    registry_detail,
    registry_edit,
    registry_list,
    registry_send_email,
)

app_name = "registry"

urlpatterns = [
    path("", registry_list , name="registry_list"),
    path("create", registry_create, name="registry_create"),
    path("<int:registry_id>", registry_detail, name="registry_detail"),
    path("<int:registry_id>/edit", registry_edit, name="registry_edit"),
    path("<int:registry_id>/delete", registry_delete , name="registry_delete"),
    path("<int:registry_id>/email", registry_send_email, name="registry_send_email"),

    path("<int:registry_id>/contact/create", registry_contact_create, name="registry_contact_create"),
    path("<int:registry_id>/contact/<int:contact_id>/edit", registry_contact_edit, name="registry_contact_edit"),
    path("<int:registry_id>/contact/<int:contact_id>/delete", registry_contact_delete, name="registry_contact_delete"),

    path("<int:registry_id>/address/create", registry_address_create, name="registry_address_create"),
    path("<int:registry_id>/address/<int:address_id>/edit", registry_address_edit, name="registry_address_edit"),
    path("<int:registry_id>/address/<int:address_id>/delete", registry_address_delete , name="registry_address_delete"),
]