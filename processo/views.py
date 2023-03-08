from datetime import date

from advogado.models import Advogado
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Processos, ProcessosHonorarios
from .serializers import *
from .utils.scraping.tj_rj import TjRjScraping


class ProcessosViewSet(ModelViewSet):
    queryset = Processos.objects.all()
    serializer_class = ProcessosSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        q = self.request.query_params.get("q", None)
        laywer = self.request.query_params.get("advogado", None)
        date_selected = self.request.query_params.get("iniciado", None)

        if q is None:
            q = ""

        laywers_qs = ""
        date_qs = ""

        if laywer is not None and laywer != "":
            try:
                laywers_qs = f"""Processos.objects.filter(
                        Q(codigo_processo__istartswith=q) |
                        Q(parte_adversa__nome__istartswith=q)|
                        Q(cliente__nome__istartswith=q)|
                        Q(municipio__istartswith=q)|
                        Q(vara__istartswith=q)
                ) & Processos.objects.filter(
                    advogado_responsavel=eval("get_object_or_404(Advogado, pk={int(laywer)})")
                    )"""
            except Advogado.DoesNotExist:
                raise NotFound()

        if date_selected is not None:
            date_selected = date_selected.split("/")
            if laywers_qs == "":
                date_qs = f"""Processos.objects.filter(
                    iniciado__gte="{date(int(date_selected[1]), int(date_selected[0]), 1)}"
                )"""
            else: 
                date_qs = f"""& Processos.objects.filter(
                    iniciado__gte="{date(int(date_selected[1]), int(date_selected[0]), 1)}"
                )"""
            
        if laywers_qs == "" and date_qs == "":
            qs = Processos.objects.filter(
                        Q(codigo_processo__istartswith=q) |
                        Q(parte_adversa__nome__istartswith=q)|
                        Q(advogado_responsavel__nome__istartswith=q)|
                        Q(cliente__nome__istartswith=q)|
                        Q(municipio__istartswith=q)|
                        Q(vara__istartswith=q)
                )
        elif laywers_qs == "" and date_qs != "":
            qs = Processos.objects.filter(
                        Q(codigo_processo__istartswith=q) |
                        Q(parte_adversa__nome__istartswith=q)|
                        Q(advogado_responsavel__nome__istartswith=q)|
                        Q(cliente__nome__istartswith=q)|
                        Q(municipio__istartswith=q)|
                        Q(vara__istartswith=q)
                ) and eval(date_qs)

        elif laywer != "" and date_qs == "":
            qs = eval(laywers_qs)

        elif laywer == "" and date_qs != "":
            qs = eval(date_qs)
        
        else: 
            qs = eval(laywers_qs + date_qs)

        return qs.order_by("-id")


@api_view(["GET", "POST"])  
def tjRjScraping(request):
    if not request.user.is_authenticated:
       return Response(data={"detail": "Você não está autenticado"}, status=401)
    if request.method == "POST":
        processos_ws = TjRjScraping("../chromedriver")
        data = processos_ws.run(request.data["codigo_processo"])
        return Response(data=data["body"], status=data["status"])

class renderPage(TemplateView):
    template_name = "index.html"

class ProcessosHonorariosViewSet(ModelViewSet):
    queryset = ProcessosHonorarios.objects.all()
    serializer_class = ProcessosHonorariosSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        q = self.request.query_params.get("q", None)
        if q == None:
            return super().get_queryset()
        try:
            qs = ProcessosHonorarios.objects.filter(processo=Processos.objects.get(pk=int(q)))
        except:
            raise NotFound()
        return qs
    
class ProcessosAnexosViewSet(ModelViewSet):
    queryset = ProcessosAnexos.objects.all()
    serializer_class = ProcessosAnexosSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        q = self.request.query_params.get("q", None)
        if q == None:
            return super().get_queryset()
        try:
            qs = ProcessosAnexos.objects.filter(processo=Processos.objects.get(pk=int(q)))
        except:
            raise NotFound()
        return qs
    