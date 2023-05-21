from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from advogado.urls import laywer_router as laywer_router

from processo.urls import processo_router as lawsuit_router
from processo.urls import processo_router_nested as lawsuit_nested_router

from cliente.urls import cliente_router as client_router
from cliente.urls import cliente_router_nested as client_router_nested

from parte_adversa.urls import parteadv_router as adverse_part_router
from parte_adversa.urls import parteadv_router_nested as adverse_part_router_nested

from project.views import login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('processo/', include("processo.urls")),
    path('cliente/', include("cliente.urls")),
    path('parte-adversa/', include("parte_adversa.urls"))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('api/v1/', include(client_router.urls)),
    path('api/v1/', include(client_router_nested.urls)),
    path('api/v1/', include(adverse_part_router.urls)),
    path('api/v1/', include(adverse_part_router_nested.urls)),
    path('api/v1/', include(lawsuit_router.urls)),
    path('api/v1/', include(lawsuit_nested_router.urls)),
    path('api/v1/', include(laywer_router.urls))
]


if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(
            title="Snippets API",
            default_version='v1',
            description="Test description",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contact@snippets.local"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )

    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]

