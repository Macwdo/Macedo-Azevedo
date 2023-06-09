from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib import messages
from django.urls import reverse
from processo.models import ProcessosHonorarios
from processo.forms import LawsuitValuesForm


@login_required
@require_http_methods(["POST"])
def lawsuit_value_create(request: HttpRequest, lawsuit_id: int):
    lawsuit_value_form = LawsuitValuesForm(request.POST, initial={'processo_id': lawsuit_id})
    
    if lawsuit_value_form.is_valid():
        lawsuit_value = lawsuit_value_form.save(commit=False)
        lawsuit_value.processo_id = lawsuit_id
        lawsuit_value.ganho = True if request.POST.get("ganho") == "on" else False
        lawsuit_value.save()
        messages.success(request, f"Valor de processo criado com sucesso.")
        return redirect(reverse("lawsuit:lawsuit_detail", kwargs={"lawsuit_id": lawsuit_id}) + "?q_values= ")
    else:
        messages.error(request, "Erro na criação do valor de processo")
        return redirect(reverse("lawsuit:lawsuit_detail", kwargs={"lawsuit_id": lawsuit_id}) + "?q_values= ")

@login_required
@require_http_methods(["POST"])
def lawsuit_value_edit(request: HttpRequest, lawsuit_id: int, lawsuit_value_id: int):
    lawsuit_value = get_object_or_404(ProcessosHonorarios, pk=lawsuit_value_id)
    lawsuit_value_form = LawsuitValuesForm(request.POST, instance=lawsuit_value)
        
    if lawsuit_value_form.is_valid():
        lawsuit_value = lawsuit_value_form.save(commit=False)
        lawsuit_value.processo_id = lawsuit_id
        lawsuit_value.ganho = True if request.POST.get("ganho") == "on" else False
        lawsuit_value.save()
        messages.success(request, f"O Valor de processo de valor {lawsuit_value} foi editado com sucesso.")
        return redirect(reverse("lawsuit:lawsuit_detail", kwargs={"lawsuit_id": lawsuit_id}) + "?q_values= ")
    else:
        messages.error(request, "Erro na edição do valor de processo")
        return redirect(reverse("lawsuit:lawsuit_detail", kwargs={"lawsuit_id": lawsuit_id}) + "?q_values= ")


@login_required
@require_http_methods(["GET"])
def lawsuit_value_delete(request: HttpRequest, lawsuit_id: int, lawsuit_value_id: int):
    lawsuit = get_object_or_404(ProcessosHonorarios, pk=lawsuit_value_id)
    try:
        messages.success(request, f"Valor de processo deletado com sucesso")
        lawsuit.delete()
    except:
        messages.error(request, f"Não foi possível deletar o valor processo {lawsuit}")
    return redirect(reverse("lawsuit:lawsuit_detail", kwargs={"lawsuit_id": lawsuit_id}) + "?q_values= ")
