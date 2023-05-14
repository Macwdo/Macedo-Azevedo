from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib import messages
from django.urls import reverse
from processo.models import Processos, ProcessosHonorarios, ProcessosAnexos
from advogado.models import Advogado
from processo.forms import LawsuitFileForm, LawsuitValuesForm

@login_required
@require_http_methods(["GET"])
def list(request: HttpRequest):
    lawsuits = Processos.objects.all()

    context = {
        "lawsuits": lawsuits
    }
    return render(request, "lawsuit_list.html", context)


@login_required
@require_http_methods(["GET"])
def detail(request: HttpRequest, pk: int):

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
@require_http_methods(["GET"])
def delete(request: HttpRequest, pk: int):
    lawsuit = Processos.objects.get(pk=pk)
    try:
        lawsuit.delete()
    except:
        messages.error(request, f"Não foi possível deletar o processo {lawsuit}")
    return redirect(reverse("lawsuits:list"))


