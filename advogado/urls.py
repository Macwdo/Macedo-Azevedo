from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import AdvogadoViewSet, getCurrentUser

router = SimpleRouter()

router.register(r"advogado", AdvogadoViewSet)


urlpatterns = [
    path("current/", getCurrentUser, name="current")
]

