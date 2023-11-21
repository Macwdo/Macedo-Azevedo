from smtplib import SMTPAuthenticationError, SMTPSenderRefused
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib import messages
from django.urls import reverse
import sentry_sdk
from utils.send_email import send_email_with_template
from registry.models import Registry, RegistryCnpj, RegistryCpf
from registry.forms import RegistryCnpjForm, RegistryCpfForm, RegistryForm, RegistryContactForm, RegistryAddressForm
from django.core.paginator import Paginator
from processo.models import Processos
from django.db.models import Q
from django.db import transaction


@login_required
@require_http_methods(["GET", "POST"])
def registry_create(request: HttpRequest):
    if request.method == "GET":
        registry_form = RegistryForm()
        registry_cpf_form = RegistryCpfForm()
        registry_cnpj_form = RegistryCnpjForm()
        
        registry_form_fields_id = [field.id_for_label for field in registry_form]
        registry_cpf_form_fields_id = [field.id_for_label for field in registry_cpf_form]
        registry_cnpj_form_fields_id = [field.id_for_label for field in registry_cnpj_form]
        
        context = {
            "registry_form": registry_form,
            "registry_cpf_form": registry_cpf_form,
            "registry_cnpj_form": registry_cnpj_form,
            "forms_fields": {
                "registry_form_fields_id": registry_form_fields_id,
                "registry_cpf_form_fields_id": registry_cpf_form_fields_id,
                "registry_cnpj_form_fields_id": registry_cnpj_form_fields_id
            }
        }
        return render(request, "registry_create_detail.html", context)
    
    if request.method == "POST":
        registry_form = RegistryForm(request.POST, request.FILES)
        registry_cpf_form = RegistryCpfForm(request.POST)
        registry_cnpj_form = RegistryCnpjForm(request.POST)
        
        try:
            with transaction.atomic():
                if registry_form.is_valid():
                    registry = registry_form.save()

                    if registry_cpf_form.is_valid():
                        cpf = registry_cpf_form.cleaned_data.get("cpf", None)
                        registry_cpf_form.cleaned_data["registry"] = registry
                        if cpf:
                            registry.registry_cpf = RegistryCpf.objects.create(**registry_cpf_form.cleaned_data)
                            
                    if registry_cnpj_form.is_valid():
                        cnpj = registry_cnpj_form.cleaned_data.get("cnpj", None)
                        registry_cnpj_form.cleaned_data["registry"] = registry
                        if cnpj:
                            registry.registry_cnpj = RegistryCnpj.objects.create(**registry_cnpj_form.cleaned_data)
                
                messages.success(request, "Registro criado com sucesso")
                return redirect(reverse("registry:registry_detail", kwargs={"registry_id": registry.pk}))
        except:
            messages.error(request, "Não foi possível efetuar a criação do registro")
            return redirect(reverse("registry:registry_create"))

@login_required
@require_http_methods(["GET"])
def registry_list(request: HttpRequest):
    registries = Registry.objects.all().order_by("-id")
    
    q = request.GET.get("q", None)
    if q:
        registries = registries.filter(name__icontains=q)

    paginator = Paginator(registries, 9)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)

    context = {
        "registries": registries,
        "page": page
    }
    return render(request, "registry_list.html", context)

@login_required
@require_http_methods(["GET"])
def registry_detail(request: HttpRequest, registry_id: int):
    registry = get_object_or_404(Registry, pk=registry_id)
    
    lawsuits_envolved = Processos.objects.filter(
        Q(cliente=registry) |
        Q(parte_adversa=registry)
    )
    registry_form = RegistryForm(instance=registry)
    registry_address_form = RegistryAddressForm()
    registry_contact_form = RegistryContactForm()
    
    try:
        registry_cpf_form = RegistryCpfForm(instance=registry.registry_cpf)
    except RegistryCpf.DoesNotExist:
        registry_cpf_form = RegistryCpfForm()
        
    try:
        registry_cnpj_form = RegistryCnpjForm(instance=registry.registry_cnpj)
    except RegistryCnpj.DoesNotExist:
        registry_cnpj_form = RegistryCnpjForm()
    
    registry_form_fields_id = [field.id_for_label for field in registry_form]
    registry_cpf_form_fields_id = [field.id_for_label for field in registry_cpf_form]
    registry_cnpj_form_fields_id = [field.id_for_label for field in registry_cnpj_form]
    

    context = {
        "registry": registry,
        "lawsuits_envolved": len(lawsuits_envolved),
        "registry_form": registry_form,
        "registry_cpf_form": registry_cpf_form,
        "registry_cnpj_form": registry_cnpj_form,
        
        "forms_fields": {
            "registry_form_fields_id": registry_form_fields_id,
            "registry_cpf_form_fields_id": registry_cpf_form_fields_id,
            "registry_cnpj_form_fields_id": registry_cnpj_form_fields_id,
        },
        
        "registry_address_form": registry_address_form,
        "registry_contact_form": registry_contact_form,
    }
    return render(request, "registry_create_detail.html", context)

@login_required
@require_http_methods(["POST"])
def registry_edit(request: HttpRequest, registry_id: int):
    registry = get_object_or_404(Registry, pk=registry_id)
    registry_form = RegistryForm(request.POST, request.FILES, instance=registry)
    registry_cpf_form = RegistryCpfForm(request.POST, instance=registry)
    registry_cnpj_form = RegistryCnpjForm(request.POST, instance=registry)
        
    if registry_form.is_valid():
        registry_form.save()
        
    if registry_cpf_form.is_valid():
        cpf = registry_cpf_form.cleaned_data.get("cpf", None)
        if cpf:
            registry_cpf = RegistryCpf.objects.filter(registry=registry)

            if registry_cpf.exists():
                registry_cpf.update(**registry_cpf_form.cleaned_data)
            else:
                registry_cpf_form.cleaned_data["registry"] = registry
                new_registry_cpf = RegistryCpf.objects.create(**registry_cpf_form.cleaned_data)
                registry.registry_cpf = new_registry_cpf
                registry.registry_cpf.save()
        
    if registry_cnpj_form.is_valid():
        cnpj = registry_cnpj_form.cleaned_data.get("cnpj", None)
        if cnpj:
            registry_cnpj = RegistryCnpj.objects.filter(registry=registry)

            if registry_cnpj.exists():
                registry_cnpj.update(**registry_cnpj_form.cleaned_data)
            else:
                registry_cnpj_form.cleaned_data["registry"] = registry
                new_registry_cnpj = RegistryCnpj.objects.create(**registry_cnpj_form.cleaned_data)
                registry.registry_cnpj = new_registry_cnpj
                registry.registry_cnpj.save()
            
    messages.success(request, "Registro editado com sucesso")
    return redirect(reverse("registry:registry_detail", kwargs={"registry_id": registry_id}))
  
@login_required
@require_http_methods(["POST"])
def registry_delete(request: HttpRequest, registry_id: int):
    registry = get_object_or_404(Registry, pk=registry_id)
    try:
        registry.delete()
        messages.success(request, f"Registro {registry.name} foi excluído com sucesso")
    except:
        messages.error(request, f"Não foi possível apagar o registro do {registry}")
    return redirect(reverse("registry:registry_list"))


@login_required
@require_http_methods(["POST"])
def registry_send_email(request: HttpRequest, registry_id):
    registry = get_object_or_404(Registry, pk=registry_id)

    destiny = request.POST.get("email", None)
    title = request.POST.get("title", None)
    text = request.POST.get("text", None)
    files = request.FILES.getlist("files[]")

    context = {
        "name": registry.name,
        "title": title,
        "text": text
    }
    
    try:
        send_email_with_template(
            registry_name=registry.name,
            destiny=destiny,
            context=context,
            files=files
        )
        messages.success(request, "Email enviado com sucesso.")
        
        return redirect(reverse("registry:registry_detail", kwargs={"registry_id": registry_id}))

    except SMTPAuthenticationError as e:
        sentry_sdk.capture_exception(e)
        messages.error(request, "Houve um erro com a senha do email raiz, favor contatar administrador.")
        
    except SMTPSenderRefused as e:
        sentry_sdk.capture_exception(e)
        messages.error(request, "Houve um erro ao enviar o email, favor contatar administrador.")








