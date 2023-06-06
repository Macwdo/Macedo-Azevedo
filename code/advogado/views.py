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
            messages.success(request, f"Advogado {lawyer.name} Registrado com sucesso.")
            return redirect(reverse("lawyer:lawyer_create"))
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
    
    context = {
        "lawyer": lawyer
    }
    
    return render(request, "lawyer_detail.html", context)
    
def lawyer_edit(request: HttpRequest):
    ...
    
def lawyer_delete(request: HttpRequest):
    ...

