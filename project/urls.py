from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from advogado.urls import router as advogado_router
from advogado.urls import urlpatterns as advogado_urls
from cliente.urls import router as cliente_router
from processo.urls import router as processo_router
from processo.views import renderPage

all_routers = processo_router.urls + cliente_router.urls + advogado_router.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('api/verify/', TokenVerifyView.as_view(), name='verify'),
    path('api/v1/', include(all_routers)),
    path('api/v1/', include("advogado.urls")),
    path('api/v1/', include("processo.urls")),
    path('api/v1/', include("usuarios.urls")),
    path('api/v1/data/', include("escritorio.urls")),
    path('', renderPage.as_view()),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
