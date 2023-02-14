from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from selenium import webdriver

from advogado.models import Advogado
from cliente.models import Cliente, ParteADV

from .models import Processos
from .serializers import ProcessosSerializer

class ProcessosSeleniumViewSet(ViewSet):

    def __init__(self, **kwargs) -> None:
        self.driver = webdriver.Chrome(executable_path="../chromedriver")
        self.URL = "https://www3.tjrj.jus.br/consultaprocessual/#/conspublica#porNumero"
        self.xpaths = {
            "unica": {
                "inputNp": "/html/body/app-root/app-consultar/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/app-codigo-processo-origem/div/div[2]/div/div/input[1]",
                "button": "/html/body/app-root/app-consultar/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div/button[1]"
            },
            "antiga": {}
            }
        self.nProcesso = None
        super().__init__(**kwargs)

    def list(self, request):

        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


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




@api_view(["GET"])
def processoWebScraping(request):

    return Response(data={"data":"qualquer"})


class renderPage(TemplateView):
    template_name = "index.html"


    

    

