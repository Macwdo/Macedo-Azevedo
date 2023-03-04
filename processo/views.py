from django.db.models import Q
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from advogado.models import Advogado

from .models import Processos
from .serializers import ProcessosSerializer
from .utils import webScraping


class ProcessosViewSet(ModelViewSet):
    queryset = Processos.objects.all()
    serializer_class = ProcessosSerializer
    permission_classes = [IsAuthenticated]
    

    def get_queryset(self):
        q = self.request.query_params.get("q", None)
        laywer = self.request.query_params.get("advogado", None)
        date_selected = self.request.query_params.get("desde", None)

        if q is None:
            q = ""
        
        laywers_qs = ""
        date_qs = ""

        if laywer is not None:
            try:
                laywers_qs = f"""Processos.objects.filter(
                        Q(codigo_processo__istartswith=q) |
                        Q(parte_adversa__nome__istartswith=q)|
                        Q(cliente__nome__istartswith=q)|
                        Q(municipio__istartswith=q)|
                        Q(vara__istartswith=q)
                ) & Processos.objects.filter(
                    advogado_responsavel=eval("Advogado.objects.get(pk=int({laywer}))")
                    )"""
            except Advogado.DoesNotExist:
                raise NotFound()

        if date_selected is not None:
            date_selected = date_selected.split("/")
            if laywers_qs == "":
                date_qs = """Processos.objects.filter(
                    iniciado__year=date_selected[1],
                    iniciado__month=date_selected[0]
                )"""
            else: 
                date_qs = """& Processos.objects.filter(
                    iniciado__year=date_selected[1],
                    iniciado__month=date_selected[0]
                )"""
            
        if laywers_qs == "" and date_qs == "":
            qs = Processos.objects.filter(
                        Q(codigo_processo__istartswith=q) |
                        Q(parte_adversa__nome__istartswith=q)|
                        Q(cliente__nome__istartswith=q)|
                        Q(municipio__istartswith=q)|
                        Q(vara__istartswith=q)
                )
        else: 
            qs = eval(laywers_qs+ date_qs)
        return qs


@api_view(["GET", "POST"])
def processosWebScraping(request):
    if not request.user.is_authenticated:
       return Response(data={"detail": "Você não está autenticado"}, status=401)
    if request.method == "POST":
        processos_ws = webScraping()
        codigo_processo = request.data["codigo_processo"]
        data = processos_ws.search(codigo_processo, request)
        return Response(data=data["body"], status=data["status"])

class renderPage(TemplateView):
    template_name = "index.html"
