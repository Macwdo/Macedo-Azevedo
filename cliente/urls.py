from rest_framework.routers import SimpleRouter
from .views import ClienteViewSet

router = SimpleRouter()
router.register(r"clientes", ClienteViewSet)

app_name = "cliente"

urlpatterns = [

]