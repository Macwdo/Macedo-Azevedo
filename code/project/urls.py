from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from advogado.urls import lawyer_router as lawyer_router


from project.views import login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('', include("processo.urls")),
    path('registros/', include("registry.urls")),
    path('advogados/', include("advogado.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
