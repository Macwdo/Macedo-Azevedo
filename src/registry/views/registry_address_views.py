from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from registry.forms import RegistryAddressForm
from registry.models import RegistryAddress


@login_required()
@require_http_methods(['POST'])
def registry_address_create(request: HttpRequest, registry_id: int):
    registry_address_form = RegistryAddressForm(request.POST)
    if registry_address_form.is_valid():
        registry_address_form.save()
        messages.success(request, 'Endereço de registro criado com sucesso')
    else:
        messages.error(
            request,
            'Não foi possível realizar a criação de endereço de registro',
        )
    return redirect(
        reverse(
            'registry:registry_detail', kwargs={'registry_id': registry_id}
        )
    )


@login_required()
@require_http_methods(['POST'])
def registry_address_edit(
    request: HttpRequest, registry_id: int, address_id: int
):
    registry_address = get_object_or_404(RegistryAddress, pk=address_id)
    registry_address_form = RegistryAddressForm(
        request.POST, instance=registry_address
    )
    if registry_address_form.is_valid():
        registry_address_form.save()
        messages.success(
            request, f'O endereço {registry_address} foi editado com sucesso'
        )
    else:
        messages.error(
            request,
            f'Não foi possível realizar a edição do endereço {registry_address}',
        )
    return redirect(
        reverse(
            'registry:registry_detail', kwargs={'registry_id': registry_id}
        )
    )


@login_required()
@require_http_methods(['POST'])
def registry_address_delete(
    request: HttpRequest, registry_id: int, address_id: int
):
    registry_address = get_object_or_404(RegistryAddress, pk=address_id)
    try:
        registry_address.delete()
        messages.success(request, 'Endereço de registro apagado com sucesso')
    except:
        messages.error(
            request,
            f'Não foi possível apagar o endereço de registro {registry_address}',
        )
    return redirect(
        reverse(
            'registry:registry_detail', kwargs={'registry_id': registry_id}
        )
    )
