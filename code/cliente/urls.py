from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import ClienteViewSet, ParteADVViewSet, sendEmail, task_test

router = SimpleRouter()
router.register(r"cliente", ClienteViewSet)
router.register(r"parteadv", ParteADVViewSet)


app_name = "cliente"

urlpatterns = [
    path("send-email/", sendEmail, name="reset"),
    path("testing/", task_test, name="reset")
] + router.urls

