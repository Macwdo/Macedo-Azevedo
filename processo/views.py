from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import ArquivoModels
import os


class indexview(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        files = ArquivoModels.objects.all()
        return {'files': files}
    

def postfiles(request):
    dados = request.FILES.get('file', None)
    if request.method == "POST" and dados is not None:
        for file in request.FILES.values():
            ArquivoModels.objects.create(files=file, nome=request.POST["nome"])
        print(request.FILES)
    return redirect(reverse('processo:home'))