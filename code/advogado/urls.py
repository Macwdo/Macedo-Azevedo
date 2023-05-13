from rest_framework.routers import SimpleRouter
from advogado.api.viewsets import AdvogadoViewSet

laywer_router = SimpleRouter()

laywer_router.register(r"advogado", AdvogadoViewSet)

urlpatterns = []
