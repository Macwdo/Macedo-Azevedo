from functools import reduce
from operator import add

from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotAuthenticated
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from advogado.api.serializers import (
    AdvogadoCurrentSerializer,
    AdvogadoSerializer,
)
from advogado.models import Advogado
from processo.models import Processos


class AdvogadoViewSet(ModelViewSet):
    queryset = Advogado.objects.all()
    serializer_class = AdvogadoSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
def getCurrentUser(request: Request):
    if request.user.is_anonymous:
        raise NotAuthenticated()
    user = User.objects.get(id=request.user.id)

    try:
        advogadoData = Advogado.objects.get(usuario=user)
    except Advogado.DoesNotExist:
        return Response(
            status=404,
            data={'detail': 'Não existe advogado vinculado a esse usuario'},
        )

    advogado_processos = Processos.objects.filter(
        advogado_responsavel=advogadoData.pk
    )

    honorarios = [processo.honorarios for processo in advogado_processos]
    if honorarios:
        honorarios = reduce(add, honorarios)
    else:
        honorarios = 0

    serializerData = {
        'nome': advogadoData.nome,
        'honorarios': honorarios,
        'processos': len(advogado_processos),
    }

    serializer = AdvogadoCurrentSerializer(data=serializerData)
    serializer.is_valid()

    return Response(data=serializer.data)
