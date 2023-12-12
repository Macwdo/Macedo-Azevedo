from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from registry.forms import RegistryContactForm
from registry.models import RegistryContact


@login_required()
@require_http_methods(['POST'])
def registry_contact_create(request: HttpRequest, registry_id: int):
    registry_contact_form = RegistryContactForm(request.POST)
    if registry_contact_form.is_valid():
        registry_contact_form.save()
        messages.success(request, 'Contato de registro criado com sucesso')
    else:
        messages.error(
            request,
            'Não foi possível realizar a criação do contato de registro',
        )
    return redirect(
        reverse(
            'registry:registry_detail', kwargs={'registry_id': registry_id}
        )
    )


@login_required()
@require_http_methods(['POST'])
def registry_contact_edit(
    request: HttpRequest, registry_id: int, contact_id: int
):
    registry_contact = get_object_or_404(RegistryContact, pk=contact_id)
    registry_contact_form = RegistryContactForm(
        request.POST, instance=registry_contact
    )
    if registry_contact_form.is_valid():
        registry_contact_form.save()
        messages.success(
            request, f'O contato {registry_contact} foi editado com sucesso'
        )
    else:
        messages.error(
            request,
            f'Não foi possível realizar a edição do contato {registry_contact}',
        )
    return redirect(
        reverse(
            'registry:registry_detail', kwargs={'registry_id': registry_id}
        )
    )


@login_required()
@require_http_methods(['POST'])
def registry_contact_delete(
    request: HttpRequest, registry_id: int, contact_id: int
):
    registry_contact = get_object_or_404(RegistryContact, pk=contact_id)
    try:
        registry_contact.delete()
        messages.success(request, 'Contato de registro apagado com sucesso')
    except:
        messages.error(
            request,
            f'Não foi possível apagar o contato do registro {registry_contact}',
        )

    return redirect(
        reverse(
            'registry:registry_detail', kwargs={'registry_id': registry_id}
        )
    )
