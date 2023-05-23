from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib import messages
from django.urls import reverse
from parte_adversa.models import AdversePartContact
from parte_adversa.forms import AdversePartContactForm


@login_required()
@require_http_methods(["POST"])
def adverse_part_contact_create(request: HttpRequest, adverse_part_id: int):
    adverse_part_contact_form = AdversePartContactForm(request.POST)
    if adverse_part_contact_form.is_valid():
        adverse_part_contact_form.save()
        messages.success(request, "Contato de adverse_part criado com sucesso")
    else:
        messages.error(request, "Não foi possível realizar a criação do contato de adverse_part")
    return redirect(reverse("adverse_part:adverse_part_detail", kwargs={"adverse_part_id": adverse_part_id}))

@login_required()
@require_http_methods(["POST"])
def adverse_part_contact_edit(request: HttpRequest, adverse_part_id: int, contact_id: int):
    adverse_part_contact = get_object_or_404(AdversePartContact, pk=contact_id)
    adverse_part_contact_form = AdversePartContactForm(request.POST, instance=adverse_part_contact)
    if adverse_part_contact_form.is_valid():
        adverse_part_contact_form.save()
        messages.success(request, f"O contato {adverse_part_contact} foi editado com sucesso")
    else:
        messages.error(request, f"Não foi possível realizar a edição do contato {adverse_part_contact}")
    return redirect(reverse("adverse_part:adverse_part_detail", kwargs={"adverse_part_id": adverse_part_id}))

@login_required()
@require_http_methods(["POST"])
def adverse_part_contact_delete(request: HttpRequest, adverse_part_id: int, contact_id: int):
    adverse_part_contact = get_object_or_404(AdversePartContact, pk=contact_id)
    try:
        adverse_part_contact.delete()
        messages.success(request, "Contato de adverse_part apagado com sucesso")
    except:
        messages.error(request, f"Não foi possível apagar o contato do adverse_part {adverse_part_contact}")

    return redirect(reverse("adverse_part:adverse_part_detail", kwargs={"adverse_part_id": adverse_part_id}))



