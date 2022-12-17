from .views import ProcessosViewSet, ProcessosArquivosViewSet
from rest_framework import routers


app_name = "processo"

router = routers.SimpleRouter()

router.register(r'processos', ProcessosViewSet)
router.register(r'arquivos', ProcessosArquivosViewSet)


urlpatterns = [
    
]
