from django.urls import include, path

from .views import home_page_view, login_view, processo_render_form

app_name = 'processo'

urlpatterns = [
    path('', login_view, name="login-page"),
    path('home/', home_page_view, name="home-page"),
    path('processo/', processo_render_form, name="processo-render-form")
]
