from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib import messages
from django.urls import reverse
from cliente.models import ClienteEndereco
from cliente.forms import ClientAddressForm


@login_required()
@require_http_methods(["POST"])
def client_address_create(request: HttpRequest, client_id: int):
    client_address_form = ClientAddressForm(request.POST)
    if client_address_form.is_valid():
        client_address_form.save()
        messages.success(request, "Endereço de cliente criado com sucesso")
    else:
        messages.error(request, "Não foi possível realizar a criação de endereço de cliente")
    return redirect(reverse("client:client_detail", kwargs={"client_id": client_id}))

@login_required()
@require_http_methods(["POST"])
def client_address_edit(request: HttpRequest, client_id: int, address_id: int):
    client_address = get_object_or_404(ClienteEndereco, pk=address_id)
    client_address_form = ClientAddressForm(request.POST, instance=client_address)
    if client_address_form.is_valid():
        client_address_form.save()
        messages.success(request, f"O endereço {client_address} foi editado com sucesso")
    else:
        messages.error(request, f"Não foi possível realizar a edição do endereço {client_address}")
    return redirect(reverse("client:client_detail", kwargs={"client_id": client_id}))

@login_required()
@require_http_methods(["POST"])
def client_address_delete(request: HttpRequest, client_id: int, address_id: int):
    client_address = get_object_or_404(ClienteEndereco, pk=address_id)
    try:
        client_address.delete()
        messages.success(request, "Endereço de cliente apagado com sucesso")
    except:
        messages.error(request, f"Não foi possível apagar o endereço do cliente {client_address}")
    return redirect(reverse("client:client_detail", kwargs={"client_id": client_id}))


