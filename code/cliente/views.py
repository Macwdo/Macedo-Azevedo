from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib import messages
from django.urls import reverse
from cliente.models import Cliente
from cliente.forms import ClientForm, ClientAddressForm, ClientContactForm
from django.core.paginator import Paginator

@login_required
@require_http_methods(["GET"])
def list(request: HttpRequest):
    clients = Cliente.objects.all().order_by("-id")
    
    q = request.GET.get("q", None)
    if q:
        clients = clients.filter(nome__icontains=q)

    paginator = Paginator(clients, 9)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)

    context = {
        "clients": clients,
        "page": page
    }
    return render(request, "client_list.html", context)


@login_required
@require_http_methods(["GET"])
def detail(request: HttpRequest, pk: int):
    client = get_object_or_404(Cliente, pk=pk)
    
    client_form = ClientForm(instance=client)
    client_address_form = ClientAddressForm()
    client_contact_form = ClientContactForm()

    context = {
        "client": client,
        "client_form": client_form,
        "client_address_form": client_address_form,
        "client_contact_form": client_contact_form
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


