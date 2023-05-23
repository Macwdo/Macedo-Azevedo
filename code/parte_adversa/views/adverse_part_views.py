from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib import messages
from django.urls import reverse
from parte_adversa.models import AdversePart
from parte_adversa.forms import AdversePartForm, AdversePartAddressForm, AdversePartContactForm
from django.core.paginator import Paginator
from processo.models import Processos


@login_required
@require_http_methods(["GET", "POST"])
def adverse_part_create(request: HttpRequest):
    if request.method == "GET":
        adverse_part_form = AdversePartForm()
        context = {
            "form": adverse_part_form
        }
        return render(request, "adverse_part_create.html", context)
    
    if request.method == "POST":
        adverse_part_form = AdversePartForm(request.POST, request.FILES)
        print(request.POST)
        if adverse_part_form.is_valid():
            new_adverse_part = adverse_part_form.save()
            messages.success(request, "Parte adversa criada com sucesso")
            return redirect(reverse("adverse_part:adverse_part_detail", kwargs={"adverse_part_pk": new_adverse_part.pk}))
        else:
            messages.error(request, "Não foi possível realizar a criação da Parte adversa")
            return redirect(reverse("adverse_part:adverse_part_create"))

@login_required
@require_http_methods(["GET"])
def adverse_part_list(request: HttpRequest):
    adverse_parts = AdversePart.objects.all().order_by("-id")
    
    q = request.GET.get("q", None)
    if q:
        adverse_parts = adverse_parts.filter(nome__icontains=q)

    paginator = Paginator(adverse_parts, 9)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)

    context = {
        "adverse_parts": adverse_parts,
        "page": page
    }
    return render(request, "adverse_part_list.html", context)

@login_required
@require_http_methods(["GET"])
def adverse_part_detail(request: HttpRequest, adverse_part_id: int):
    adverse_part = get_object_or_404(AdversePart, pk=adverse_part_id)
    
    lawsuits_envolved = Processos.objects.filter(parte_adversa=adverse_part)
    adverse_part_form = AdversePartForm(instance=adverse_part)
    adverse_part_address_form = AdversePartAddressForm()
    adverse_part_contact_form = AdversePartContactForm()

    context = {
        "adverse_part": adverse_part,
        "lawsuits_envolved": len(lawsuits_envolved),
        "adverse_part_form": adverse_part_form,
        "adverse_part_address_form": adverse_part_address_form,
        "adverse_part_contact_form": adverse_part_contact_form
    }
    return render(request, "adverse_part_detail.html", context)

@login_required
@require_http_methods(["POST"])
def adverse_part_edit(request: HttpRequest, adverse_part_id: int):
    adverse_part = get_object_or_404(AdversePart, pk=adverse_part_id)
    adverse_part_form = AdversePartForm(request.POST, request.FILES, instance=adverse_part)
    if adverse_part_form.is_valid():
        adverse_part_form.save()
        messages.success(request, f"adverse_part {adverse_part.nome} editado com sucesso")
    else:
        messages.error(request, f"Não foi possível realizar a edição da Parte adversa {adverse_part.nome}")
    return redirect(reverse("adverse_part:adverse_part_detail", kwargs={"adverse_part_id": adverse_part_id}))

@login_required
@require_http_methods(["POST"])
def adverse_part_delete(request: HttpRequest, adverse_part_id: int):
    adverse_part = get_object_or_404(AdversePart, pk=adverse_part_id)
    try:
        adverse_part.delete()
        messages.success(request, f"adverse_part {adverse_part.nome} foi excluído com sucesso")
    except:
        messages.error(request, f"Não foi possível apagar o registro da Parte adversa {adverse_part}")
    return redirect(reverse("adverse_part:adverse_part_list"))


