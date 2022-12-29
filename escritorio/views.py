from rest_framework.viewsets import ModelViewSet
from escritorio.models import Custos
from advogado.models import Advogado
from processo.models import Processos
from escritorio.serializers import CustosSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.exceptions import AuthenticationFailed

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
    if request.user.is_anonymous:
        raise AuthenticationFailed()
    advogados = Advogado.objects.all()
    advdict = {}
    total = 0
    for adv in advogados:
        advdict[adv.nome] = adv.honorarios
        total += adv.honorarios
    hondict ={}
    hondict["total"] = sum(advdict.values())
    hondict["advogados"] = advdict
    return JsonResponse(hondict, safe=True, status=200)
        
@api_view(["GET"])
def sofProcessos(request):
    if request.user.is_anonymous:
        raise AuthenticationFailed()
    advogados = Advogado.objects.all()
    prcsdict = {}
    for adv in advogados:
        prcsdict[adv.nome] = len(Processos.objects.filter(advogado_responsavel=adv.pk))

    return JsonResponse(prcsdict, safe=True, status=200)

@api_view(["GET"])
def sofCustos(request):
    if request.user.is_anonymous:
        raise AuthenticationFailed()
    custos = Custos.objects.all()
    custdict_pago = {}
    custdict_npago = {}
    total = 0
    for custo in custos:
        if custo.pago:
            custdict_pago[custo.nome_custo] = custo.custo
        else:
            custdict_npago[custo.nome_custo] = custo.custo
        total += custo.custo

    custosdict = {"total":total}
    custosdict["pago"] = custdict_pago
    custosdict["nao_pago"] = custdict_npago

    return JsonResponse(custosdict, safe=True, status=200)


#sof Receita e Lucro


