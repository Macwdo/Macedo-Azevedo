from django.urls import path
from .views import indexview, postfiles
from django.conf import settings
from django.conf.urls.static import static

app_name = "processo"

urlpatterns = [
    path('', indexview.as_view(), name="home"),
    path('upload/', postfiles, name="upload"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


