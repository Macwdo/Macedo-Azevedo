from rest_framework.viewsets import ModelViewSet
from escritorio.models import Custos
from advogado.models import Advogado
from processo.models import Processos
from escritorio.serializers import CustosSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.http import JsonResponse

class CustosViewSet(ModelViewSet):
    queryset = Custos.objects.all()
    serializer_class = CustosSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        fields = {}
        for k, v in self.request.query_params.items():
            fields[k + "__icontains"] = v
        qs = Custos.objects.filter(**fields)
        return qs
#sof = SUM OF

@api_view(["GET"])
def sofHonorarios(request):
    advogados = Advogado.objects.all()
    advdict = {}
    for adv in advogados:
        advdict[adv.nome] = adv.honorarios

    advdict["total"] = sum(advdict.values())
    return JsonResponse(advdict, safe=True, status=200)
        
@api_view(["GET"])
def sofProcessos(request):
    advogados = Advogado.objects.all()
    prcsdict = {}
    for adv in advogados:
        prcsdict[adv.nome] = len(Processos.objects.filter(advogado_responsavel=adv.pk))

    return JsonResponse(prcsdict, safe=True, status=200)


