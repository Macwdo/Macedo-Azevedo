from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib import messages
from django.urls import reverse


@login_required
@require_http_methods(["GET"])
def list(request: HttpRequest):
    messages.success(request, "Criado com sucesso")
    return render(request, "lawsuits/lawsuit_list.html")
