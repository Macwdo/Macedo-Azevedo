from django.http import HttpRequest
from django.shortcuts import render
from advogado.forms import LawyerForm
from advogado.models import Advogado


def lawyer_create(request: HttpRequest):
    form = LawyerForm()
    context = {
        "form": form
    }
    return render(request, "lawyer_create.html", context)
    

def lawyer_list(request: HttpRequest):
    lawyers = Advogado.objects.all()
    context = {
        "lawyers": lawyers
    }
    return render(request, "lawyer_list.html", context)

def lawyer_detail(request: HttpRequest):
    ...
    
def lawyer_edit(request: HttpRequest):
    ...
    
def lawyer_delete(request: HttpRequest):
    ...

