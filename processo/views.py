from random import randint

from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from advogado.models import Advogado
from cliente.models import Cliente, ParteADV

from .models import Processos, ProcessosArquivos


def criarprocesso(request):
    # Processos.objects.create(
    #     codigo_processo = f"{randint(0, 1000)} {randint(0, 1000)}",
    #     advogado_responsavel = Advogado.objects.get(pk=1),
    #     parte_adversa = Cliente.objects.get(pk=1),
    #     cliente = ParteADV.objects.get(pk=2),
    #     posicao = "Autor",
    #     assunto = "Civil",
    #     municipio = "Rio de janeiro",
    #     estado = "RJ",
    #     n_vara = "40",
    #     vara = "Vara do trabalho",
    # )
    processos = Processos.objects.all()
    print(ProcessosArquivos.objects.all()[0].arquivos)
    return render(request,"index.html",{"processos": processos})
    
