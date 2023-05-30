from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib import messages
from django.urls import reverse
from registry.models import Registry, RegistryCnpj, RegistryCpf
from registry.forms import RegistryForm, RegistryContactForm, RegistryAddressForm
from django.core.paginator import Paginator
from processo.models import Processos

@login_required
@require_http_methods(["GET", "POST"])
def registry_create(request: HttpRequest):
    if request.method == "GET":
        registry_form = RegistryForm()
        context = {
            "form": registry_form
        }
        return render(request, "registry_create.html", context)
    
    if request.method == "POST":
        registry_form = RegistryForm(request.POST, request.FILES)
        if registry_form.is_valid():
            registry = registry_form.save()
            
            cpf = request.POST.get("cpf", None)
            cnpj = request.POST.get("cnpj", None)
            
            if cpf:
                registry.cpf = RegistryCpf.objects.create(registry=registry, cpf=cpf)
                
            if cnpj:
                registry.cnpj = RegistryCnpj.objects.create(registry=registry, cnpj=cnpj)
                
            registry.save()
            
            messages.success(request, "Registro criado com sucesso")
            return redirect(reverse("registry:registry_detail", kwargs={"registry_id": registry.pk}))
        else:
            messages.error(request, "Não foi possível realizar um novo registro")
            return redirect(reverse("registry:registry_create"))

@login_required
@require_http_methods(["GET"])
def registry_list(request: HttpRequest):
    registrys = Registry.objects.all().order_by("-id")
    
    q = request.GET.get("q", None)
    if q:
        registrys = registrys.filter(name__icontains=q)

    paginator = Paginator(registrys, 9)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)

    context = {
        "registrys": registrys,
        "page": page
    }
    return render(request, "registry_list.html", context)

@login_required
@require_http_methods(["GET"])
def registry_detail(request: HttpRequest, registry_id: int):
    registry = get_object_or_404(Registry, pk=registry_id)
    
    lawsuits_envolved = Processos.objects.filter(cliente=registry)
    registry_form = RegistryForm(instance=registry)
    registry_address_form = RegistryAddressForm()
    registry_contact_form = RegistryContactForm()

    context = {
        "registry": registry,
        "lawsuits_envolved": len(lawsuits_envolved),
        "registry_form": registry_form,
        "registry_address_form": registry_address_form,
        "registry_contact_form": registry_contact_form
    }
    return render(request, "registry_detail.html", context)

@login_required
@require_http_methods(["POST"])
def registry_edit(request: HttpRequest, registry_id: int):
    registry = get_object_or_404(Registry, pk=registry_id)
    registry_form = RegistryForm(request.POST, request.FILES, instance=registry)
    if registry_form.is_valid():
        registry = registry_form.save()
        cpf = request.POST.get("cpf", None)
        cnpj = request.POST.get("cnpj", None)
        
        if cpf:
            registry.cpf.cpf = cpf
            registry.cpf.save()
            
        if cnpj:
            registry.cnpj.cnpj = cnpj
            registry.cnpj.save()
            
        registry.save()
        messages.success(request, f"Registry {registry.name} editado com sucesso")
    else:
        messages.error(request, f"Não foi possível realizar a edição do registry {registry.name}")
    return redirect(reverse("registry:registry_detail", kwargs={"registry_id": registry_id}))

@login_required
@require_http_methods(["POST"])
def registry_delete(request: HttpRequest, registry_id: int):
    registry = get_object_or_404(Registry, pk=registry_id)
    try:
        registry.delete()
        messages.success(request, f"Registry {registry.name} foi excluído com sucesso")
    except:
        messages.error(request, f"Não foi possível apagar o registro do registry {registry}")
    return redirect(reverse("registry:registry_list"))


