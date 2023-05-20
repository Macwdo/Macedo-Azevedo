from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib import messages
from django.urls import reverse
from cliente.models import Cliente
from cliente.forms import ClientForm

@login_required
@require_http_methods(["GET"])
def list(request: HttpRequest):
    clients = Cliente.objects.all()
    
    q = request.GET.get("q", None)
    if q:
        clients = clients.filter(nome__icontains=q)

    context = {
        "clients": clients
    }
    return render(request, "client_list.html", context)


@login_required
@require_http_methods(["GET"])
def detail(request: HttpRequest, pk: int):
    client = get_object_or_404(Cliente, pk=pk)
    form = ClientForm()
    context = {
        "client": client,
        "form": form
    }
    return render(request, "client_detail.html", context)


@login_required
@require_http_methods(["GET"])
def delete(request: HttpRequest, pk: int):
    client = get_object_or_404(Cliente, pk=pk)
    try:
        client.delete()
    except:
        messages.error(request, f"Não foi possível apagar o registro do cliente {client}")
    return redirect(reverse("client:list"))


