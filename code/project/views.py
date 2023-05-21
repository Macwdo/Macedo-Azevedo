from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib import auth
from user.authentication import EmailAuthBackend
from django.contrib import messages
from django.urls import reverse

@require_http_methods(["GET", "POST"])
def login(request: HttpRequest):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, "login/login.html")
    if request.method == "POST":
        email: str | None = request.POST.get("email", None)
        password: str | None = request.POST.get("password", None)
        user = EmailAuthBackend().authenticate(request, email=email, password=password)
        if user:
            auth.login(request, user, backend="user.authentication.EmailAuthBackend")
            messages.success(request, f"Logado com sucesso!")
            return redirect(reverse("lawsuit:list"))
        messages.error(request, "Erro ao realizar login")
        return redirect(reverse("login"))

@login_required
@require_http_methods(["POST"])
def logout(request: HttpRequest):
    auth.logout(request)
    return redirect(reverse("login"))

@login_required
@require_http_methods(["GET"])
def repository_history(request: HttpRequest):
    "https://api.github.com/repos/macwdo/Macedo-azevedo"
