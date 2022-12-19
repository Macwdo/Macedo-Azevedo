from rest_framework.routers import SimpleRouter
from .views import ClienteViewSet, ParteADVViewSet

router = SimpleRouter()
router.register(r"clientes", ClienteViewSet)
router.register(r"parteadv", ParteADVViewSet)


app_name = "cliente"

urlpatterns = [

]