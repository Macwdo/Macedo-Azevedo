from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from parte_adversa.api.viewsets import ParteADVEnderecoViewSet, ParteADVViewSet
from django.urls import path
from parte_adversa.views import list, detail, delete
app_name = "adverse_part"


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
    path("", list, name="list"),
    path("<int:pk>", detail, name="detail"),
    path("<int:pk>/delete", delete , name="delete")
]
