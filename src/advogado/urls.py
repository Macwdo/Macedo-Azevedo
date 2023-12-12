from django.urls import path
from rest_framework.routers import SimpleRouter

from advogado.api.viewsets import AdvogadoViewSet
from advogado.views import (
    lawyer_create,
    lawyer_delete,
    lawyer_detail,
    lawyer_edit,
    lawyer_list,
)

lawyer_router = SimpleRouter()

app_name = "lawyer"

lawyer_router.register(r"advogado", AdvogadoViewSet)

urlpatterns = [
    path("create", lawyer_create, name="lawyer_create"),
    path("", lawyer_list, name="lawyer_list"),
    path("<int:lawyer_id>", lawyer_detail, name="lawyer_detail"),
    path("<int:lawyer_id>/edit", lawyer_edit, name="lawyer_edit"),
    path("<int:lawyer_id>/delete", lawyer_delete, name="lawyer_delete"),
]
