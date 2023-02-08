from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advogado.models import Advogado
from cliente.models import Cliente, ParteADV

from .models import Processos, ProcessosArquivos
from .serializers import ProcessosArquivosSerializer, ProcessosSerializer


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



class ProcessosArquivosViewSet(ModelViewSet):
    queryset = ProcessosArquivos.objects.all()
    serializer_class = ProcessosArquivosSerializer
    permission_classes = [IsAuthenticated]

class renderPage(TemplateView):
    template_name = "index.html"


    

    

