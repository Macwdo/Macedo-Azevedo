from django.urls import path, include
from .views import ProcessosViewSet, ProcessosArquivosViewSet
from rest_framework import routers


app_name = "processo"

router = routers.SimpleRouter()

router.register(r'', ProcessosViewSet)
router.register(r'arquivos', ProcessosArquivosViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),


]



