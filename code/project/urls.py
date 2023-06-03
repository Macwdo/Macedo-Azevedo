from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions

from advogado.urls import laywer_router as laywer_router

from processo.urls import processo_router as lawsuit_router
from processo.urls import processo_router_nested as lawsuit_nested_router

from project.views import login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('', include("processo.urls")),
    path('registros/', include("registry.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
