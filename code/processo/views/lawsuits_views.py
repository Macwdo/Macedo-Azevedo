from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib import messages
from django.urls import reverse
from processo.models import Processos, ProcessosHonorarios, ProcessosAnexos
from advogado.models import Advogado
from processo.forms import LawsuitFileForm, LawsuitValuesForm, LawsuitForm
from django.core.paginator import Paginator

@login_required
@require_http_methods(["GET", "POST"])
def lawsuit_create(request: HttpRequest):
    if request.method == "GET":
        form = LawsuitForm()
        context = {
            "form": form
        }
        return render(request, "lawsuit_create.html", context)
    else:
        form = LawsuitForm(request.POST)
        context = {
            "form": form
        }
        if form.is_valid():
            lawsuit = form.save()
            messages.success(request, f"O Processo de código {lawsuit.codigo_processo} foi criado com sucesso.")
            return redirect(reverse("lawsuit:lawsuit_detail", kwargs={"pk": lawsuit.pk}))
        messages.error(request, "Erro na criação do processo")
        return render(request, "lawsuit_create.html", context)


@login_required
@require_http_methods(["GET"])
def lawsuit_list(request: HttpRequest):
    lawsuits = Processos.objects.all()

    paginator = Paginator(lawsuits, 10)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    context = {
        "lawsuits": lawsuits,
        "page": page
    }
    return render(request, "lawsuit_list.html", context)


@login_required
@require_http_methods(["GET"])
def lawsuit_detail(request: HttpRequest, pk: int):

    lawsuit = get_object_or_404(Processos, pk=pk)
    lawyers = Advogado.objects.all()

    lawsuit_values = ProcessosHonorarios.objects.filter(processo=lawsuit)
    lawsuit_values_form = LawsuitValuesForm()

    lawsuit_files = ProcessosAnexos.objects.filter(processo=lawsuit)
    lawsuit_files_form = LawsuitFileForm()

    context = {
        "lawsuit": lawsuit,
        "lawyers": lawyers,
        "lawsuit_values": lawsuit_values,
        "lawsuit_values_form":lawsuit_values_form ,
        "lawsuit_files": lawsuit_files,
        "lawsuit_files_form": lawsuit_files_form
    }

    return render(request, "lawsuit_detail.html", context)

@login_required
@require_http_methods(["GET", "POST"])
def lawsuit_edit(request: HttpRequest, pk: int):
    lawsuit = get_object_or_404(Processos, pk=pk)
    if request.method == "GET":
        form = LawsuitForm(instance=lawsuit)
        context = {
                "form": form,
                "lawsuit": lawsuit
            }
        return render(request, "lawsuit_create.html", context)
    else:
        form = LawsuitForm(request.POST, instance=lawsuit)
        if form.is_valid():
            lawsuit = form.save()
            messages.success(request, f"O Processo de código {lawsuit.codigo_processo} foi editado com sucesso.")
            return redirect(reverse("lawsuit:lawsuit_detail", kwargs={"pk": lawsuit.pk}))
        messages.error(request, "Erro na edição do processo")
        context = {
                "form": form,
                "lawsuit": lawsuit
        }
        return render(request, "lawsuit_create.html", context)

@login_required
@require_http_methods(["GET"])
def lawsuit_delete(request: HttpRequest, pk: int):
    lawsuit = Processos.objects.get(pk=pk)
    try:
        lawsuit.delete()
    except:
        messages.error(request, f"Não foi possível deletar o processo {lawsuit}")
    return redirect(reverse("lawsuit:lawsuit_list"))


