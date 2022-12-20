from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static
from processo.urls import router as processo_router
from cliente.urls import router as cliente_router
from advogado.urls import router as advogado_router
from processo.views import renderPage
all_routers = processo_router.urls + cliente_router.urls + advogado_router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('api/v1/', include(all_routers)),
    path('', renderPage.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
