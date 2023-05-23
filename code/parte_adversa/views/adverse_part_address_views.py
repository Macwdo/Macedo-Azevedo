from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib import messages
from django.urls import reverse
from parte_adversa.models import AdversePartAddress
from parte_adversa.forms import AdversePartAddressForm

@login_required()
@require_http_methods(["POST"])
def adverse_part_address_create(request: HttpRequest, adverse_part_id: int):
    adverse_part_address_form = AdversePartAddressForm(request.POST)
    if adverse_part_address_form.is_valid():
        adverse_part_address_form.save()
        messages.success(request, "Endereço de adverse_part criado com sucesso")
    else:
        messages.error(request, "Não foi possível realizar a criação de endereço de adverse_part")
    return redirect(reverse("adverse_part:adverse_part_detail", kwargs={"adverse_part_id": adverse_part_id}))

@login_required()
@require_http_methods(["POST"])
def adverse_part_address_edit(request: HttpRequest, adverse_part_id: int, address_id: int):
    adverse_part_address = get_object_or_404(AdversePartAddress, pk=address_id)
    adverse_part_address_form = AdversePartAddressForm(request.POST, instance=adverse_part_address)
    if adverse_part_address_form.is_valid():
        adverse_part_address_form.save()
        messages.success(request, f"O endereço {adverse_part_address} foi editado com sucesso")
    else:
        messages.error(request, f"Não foi possível realizar a edição do endereço {adverse_part_address}")
    return redirect(reverse("adverse_part:adverse_part_detail", kwargs={"adverse_part_id": adverse_part_id}))

@login_required()
@require_http_methods(["POST"])
def adverse_part_address_delete(request: HttpRequest, adverse_part_id: int, address_id: int):
    adverse_part_address = get_object_or_404(AdversePartAddress, pk=address_id)
    try:
        adverse_part_address.delete()
        messages.success(request, "Endereço de adverse_part apagado com sucesso")
    except:
        messages.error(request, f"Não foi possível apagar o endereço do adverse_part {adverse_part_address}")
    return redirect(reverse("adverse_part:adverse_part_detail", kwargs={"adverse_part_id": adverse_part_id}))


