from rest_framework.routers import SimpleRouter
from .views import AdvogadoViewSet
router = SimpleRouter()

router.register(r"advogados", AdvogadoViewSet)


urlpatterns = [
    
]