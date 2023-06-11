from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from advogado.forms import LawyerForm
from advogado.models import Advogado
from django.contrib import messages
from django.core.paginator import Paginator


def lawyer_create(request: HttpRequest):
    if request.method == "GET":
        form = LawyerForm()
        context = {
            "form": form
        }
    else:
        form = LawyerForm(request.POST, request.FILES)
        context = {
            "form": form
        }
        if form.is_valid():
            lawyer = form.save()

            cpf = request.POST.get("cpf", None)


            messages.success(request, f"Advogado {lawyer.name} Registrado com sucesso.")
            return redirect(reverse("lawyer:lawyer_list"))
        else:
            messages.error(request, "Erro na criação do advogado")
            return render(request, "lawyer_create.html", context)

    return render(request, "lawyer_create.html", context)
    

def lawyer_list(request: HttpRequest):
    lawyers = Advogado.objects.all()
    paginator = Paginator(lawyers, 10)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    context = {
        "lawyers": lawyers,
        "page": page
    }
    return render(request, "lawyer_list.html", context)


def lawyer_detail(request: HttpRequest, lawyer_id):
    lawyer = get_object_or_404(Advogado, pk=lawyer_id)
    lawyer_form = LawyerForm(instance=lawyer)
    
    context = {
        "lawyer": lawyer,
        "lawyer_form": lawyer_form
    }
    
    return render(request, "lawyer_detail.html", context)


def lawyer_edit(request: HttpRequest, lawyer_id: int):
    lawyer = get_object_or_404(Advogado, pk=lawyer_id)
    lawyer_form = LawyerForm(request.POST, request.FILES, instance=lawyer)

    if lawyer_form.is_valid():
        lawyer = lawyer_form.save()
        messages.success(request, f"Advogado {lawyer.name} editado com sucesso")
    else:
        messages.success(request, f"Não foi possível realizar a edição do advogado {lawyer.name}")

    return redirect(reverse("lawyer:lawyer_detail", kwargs={"lawyer_id": lawyer_id}))


def lawyer_delete(request: HttpRequest, lawyer_id: int):
    lawyer = get_object_or_404(Advogado, pk=lawyer_id)
    try:
        lawyer.delete()
        messages.success(request, f"Advogado {lawyer.name} foi excluído com sucesso")
    except:
        messages.error(request, f"Não foi possível apagar o registro do { lawyer.name }")
    return redirect(reverse("lawyer:lawyer_list"))



