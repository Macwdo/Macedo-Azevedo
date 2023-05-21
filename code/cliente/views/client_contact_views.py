from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib import messages
from django.urls import reverse
from cliente.models import ClienteContato
from cliente.forms import ClientContactForm


@login_required()
@require_http_methods(["POST"])
def client_contact_create(request: HttpRequest, client_id: int):
    client_contact_form = ClientContactForm(request.POST)
    if client_contact_form.is_valid():
        client_contact_form.save()
        messages.success(request, "Contato de cliente criado com sucesso")
    else:
        messages.error(request, "Não foi possível realizar a criação do contato de cliente")
    return redirect(reverse("client:client_detail", kwargs={"client_id": client_id}))

@login_required()
@require_http_methods(["POST"])
def client_contact_edit(request: HttpRequest, client_id: int, contact_id: int):
    client_contact = get_object_or_404(ClienteContato, pk=contact_id)
    client_contact_form = ClientContactForm(request.POST, instance=client_contact)
    if client_contact_form.is_valid():
        client_contact_form.save()
        messages.success(request, f"O contato {client_contact} foi editado com sucesso")
    else:
        messages.error(request, f"Não foi possível realizar a edição do contato {client_contact}")
    return redirect(reverse("client:client_detail", kwargs={"client_id": client_id}))

@login_required()
@require_http_methods(["POST"])
def client_contact_delete(request: HttpRequest, client_id: int, contact_id: int):
    client_contact = get_object_or_404(ClienteContato, pk=contact_id)
    try:
        client_contact.delete()
        messages.success(request, "Contato de cliente apagado com sucesso")
    except:
        messages.error(request, f"Não foi possível apagar o contato do cliente {client_contact}")

    return redirect(reverse("client:client_detail", kwargs={"client_id": client_id}))



