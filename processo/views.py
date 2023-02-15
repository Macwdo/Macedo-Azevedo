from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from advogado.models import Advogado
from cliente.models import Cliente, ParteADV

from .models import Processos
from .serializers import ProcessosSerializer
from .utils import webScraping


class ProcessosViewSet(ModelViewSet):
    queryset = Processos.objects.all()
    serializer_class = ProcessosSerializer
    permission_classes = [IsAuthenticated]
# 
    def get_queryset(self):
        fields = {}
        fk_fields = {  
            "cliente": Cliente,
            "parte_adversa": ParteADV,
            "advogado_responsavel": Advogado,
            "colaborador": Advogado
        }
        for k, v in self.request.query_params.items():
            if k in fk_fields.keys():
                fields[k] = fk_fields[k].objects.filter(nome__icontains=v).first()
            else:
                fields[k + "__icontains"] = v

        qs = Processos.objects.filter(**fields)
        return qs


@api_view(["POST"])
def processosWebScraping(request):
    if request.method == "POST":
        processos_ws = webScraping()
        dataScrap1 = processos_ws.search("0000903-19.2022.8.19.0209", request)
        dataScrap2 = processos_ws.search("0030307-60.2022.8.19.0001", request)
        dataTotal = [dataScrap1, dataScrap2]
        return Response(data=dataTotal)



class renderPage(TemplateView):
    template_name = "index.html"


    

    

