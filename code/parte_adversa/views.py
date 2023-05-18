from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib import messages
from django.urls import reverse
from parte_adversa.models import ParteAdv, ParteAdvEndereco

@login_required
@require_http_methods(["GET"])
def list(request: HttpRequest):
    adverse_parts = ParteAdv.objects.all()

    context = {
        "adverse_parts": adverse_parts
    }
    return render(request, "adverse_part_list.html", context)


@login_required
@require_http_methods(["GET"])
def detail(request: HttpRequest, pk: int):
    adverse_part = get_object_or_404(ParteAdv, pk=pk)

    context = {
        "adverse_part": adverse_part
    }

    return render(request, "adverse_part_detail.html", context)


@login_required
@require_http_methods(["GET"])
def delete(request: HttpRequest, pk: int):
    adverse_part = get_object_or_404(ParteAdv, pk=pk)

    try:
        adverse_part.delete()
    except:
        messages.error(request, f"Não foi possível deletar o registro de {adverse_part}")
    return redirect(reverse("adverse_part:list"))


