from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib import messages
from django.urls import reverse
from processo.models import ProcessosAnexos
from processo.forms import LawsuitFileForm


@login_required
@require_http_methods(["POST"])
def lawsuit_file_create(request: HttpRequest, lawsuit_id: int):
    lawsuit_file_form = LawsuitFileForm(request.POST, request.FILES)
    
    if lawsuit_file_form.is_valid():
        lawsuit_file = lawsuit_file_form.save(commit=False)
        lawsuit_file.processo_id = lawsuit_id
        lawsuit_file.save()
        messages.success(request, f"Arquivo de processo criado com sucesso.")
        return redirect(reverse("lawsuit:lawsuit_detail", kwargs={"lawsuit_id": lawsuit_id}) + "?q_files= ")
    else:
        messages.error(request, "Erro na criação do Arquivo de processo")
        return redirect(reverse("lawsuit:lawsuit_detail", kwargs={"lawsuit_id": lawsuit_id}) + "?q_files= ")

@login_required
@require_http_methods(["POST"])
def lawsuit_file_edit(request: HttpRequest, lawsuit_id: int, lawsuit_file_id: int):
    lawsuit_file = get_object_or_404(ProcessosAnexos, pk=lawsuit_file_id)
    lawsuit_file_form = LawsuitFileForm(request.POST, request.FILES, instance=lawsuit_file)
    
    if lawsuit_file_form.is_valid():
        lawsuit_file = lawsuit_file_form.save(commit=False)
        lawsuit_file.processo_id = lawsuit_id
        lawsuit_file.save()
        messages.success(request, f"O Arquivo de processo {lawsuit_file} foi editado com sucesso.")
        return redirect(reverse("lawsuit:lawsuit_detail", kwargs={"lawsuit_id": lawsuit_id}) + "?q_files= ")
    else:
        messages.error(request, "Erro na edição do Arquivo de processo")
        return redirect(reverse("lawsuit:lawsuit_detail", kwargs={"lawsuit_id": lawsuit_id}) + "?q_files= ")


@login_required
@require_http_methods(["GET"])
def lawsuit_file_delete(request: HttpRequest, lawsuit_id: int, lawsuit_file_id: int):
    lawsuit = get_object_or_404(ProcessosAnexos, pk=lawsuit_file_id)
    try:
        messages.success(request, f"Arquivo de processo deletado com sucesso")
        lawsuit.delete()
    except:
        messages.error(request, f"Não foi possível deletar o Arquivo processo {lawsuit}")
    return redirect(reverse("lawsuit:lawsuit_detail", kwargs={"lawsuit_id": lawsuit_id}), + "?q_files= ")
