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
@require_http_methods(["GET", "POST"])
def client_create(request: HttpRequest):
    if request.method == "GET":
        client_form = ClientForm()
        context = {
            "form": client_form
        }
        return render(request, "client_create.html", context)
    
    if request.method == "POST":
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            new_client = client_form.save()
            messages.success(request, "Cliente criado com sucesso")
            return redirect(reverse("client:client_detail", kwargs={"pk": new_client.pk}))
        else:
            messages.error(request, "Não foi possível realizar a criação do cliente")
            return redirect(reverse("client:client_create"))

@login_required
@require_http_methods(["GET"])
def client_list(request: HttpRequest):
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
def client_detail(request: HttpRequest, client_id: int):
    client = get_object_or_404(Cliente, pk=client_id)
    
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
@require_http_methods(["POST"])
def client_edit(request: HttpRequest, client_id: int):
    client = get_object_or_404(Cliente, pk=client_id)
    client_form = ClientForm(request.POST, instance=client)
    if client_form.is_valid():
        client_form.save()
        messages.success(request, f"Cliente {client.nome} editado com sucesso")
    else:
        messages.error(request, f"Não foi possível realizar a edição do cliente {client.nome}")
    return redirect(reverse("client:client_detail", kwargs={"client_id": client_id}))

@login_required
@require_http_methods(["POST"])
def client_delete(request: HttpRequest, client_id: int):
    client = get_object_or_404(Cliente, pk=client_id)
    try:
        client.delete()
        messages.success(request, f"Cliente {client.nome} foi excluído com sucesso")
    except:
        messages.error(request, f"Não foi possível apagar o registro do cliente {client}")
    return redirect(reverse("client:client_list"))


