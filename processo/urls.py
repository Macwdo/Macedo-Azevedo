from django.urls import include, path
from rest_framework import routers

from .views import ProcessosViewSet

app_name = "processo"

router = routers.SimpleRouter()

router.register(r'processo', ProcessosViewSet)


urlpatterns = [
]
