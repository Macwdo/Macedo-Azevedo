from rest_framework.routers import SimpleRouter
from .views import AdvogadoViewSet
router = SimpleRouter()

router.register(r"advogado", AdvogadoViewSet)


urlpatterns = [
    
]