from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib import messages
from django.urls import reverse
from processo.models import Processos


@login_required
@require_http_methods(["GET"])
def list(request: HttpRequest):
    lawsuits = Processos.objects.all()

    context = {
        "lawsuits": lawsuits
    }
    

    return render(request, "lawsuits/lawsuit_list.html", context)


@login_required
@require_http_methods(["GET"])
def detail(request: HttpRequest, pk: int):

    lawsuit = get_object_or_404(Processos, pk=pk)
    context = {
        "lawsuit": lawsuit
    }

    return render(request, "lawsuits/lawsuit_detail.html", context)


@login_required
@require_http_methods(["GET"])
def delete(request: HttpRequest, pk: int):
    lawsuit = Processos.objects.get(pk=pk)
    try:
        lawsuit.delete()
    except:
        messages.error(request, f"Não foi possível deletar o processo {lawsuit}")
    return redirect(reverse("lawsuits:list"))


