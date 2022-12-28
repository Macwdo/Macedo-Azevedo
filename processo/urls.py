from .views import ProcessosViewSet, ProcessosArquivosViewSet
from rest_framework import routers
from django.urls import path, include

app_name = "processo"

router = routers.SimpleRouter()

router.register(r'processo', ProcessosViewSet)
router.register(r'arquivo', ProcessosArquivosViewSet)


urlpatterns = [
]
