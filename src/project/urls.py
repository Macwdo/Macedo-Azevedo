from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from advogado.urls import lawyer_router as lawyer_router
from processo.urls import processo_router, processo_router_nested
from project.views import login, logout

api_v1_urls = []

api_v1_urls += lawyer_router.urls

api_v1_urls += processo_router.urls
api_v1_urls += processo_router_nested.urls

api_urls = [
    path('api/v1/', include(api_v1_urls)),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh', TokenRefreshView.as_view(), name='token_refresh_pair')
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('', include("processo.urls")),
    path('registros/', include("registry.urls")),
    path('advogados/', include("advogado.urls")),
] + api_urls


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
