from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from processo.models import Processos

from .models import Advogado
from .serializer import AdvogadoCurrentSerializer, AdvogadoSerializer


class AdvogadoViewSet(ModelViewSet):
    queryset = Advogado.objects.all()
    serializer_class = AdvogadoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        fields = {}
        for k, v in self.request.query_params.items():
            fields[k + "__icontains"] = v
        qs = Advogado.objects.filter(**fields)
        return qs
    
@api_view(["GET"])
def getCurrentUser(request):
    if request.user.is_anonymous:
       return Response(status=401)
    user = User.objects.get(id=request.user.id)

    try:
        advogadoData = Advogado.objects.get(usuario=user)
    except Advogado.DoesNotExist:
        return Response(status=404) 

    serializerData = {
        "nome": advogadoData.nome,
        "honorarios": advogadoData.honorarios,
        "processos": len(Processos.objects.filter(advogado_responsavel=advogadoData.pk))
    }

    serializer = AdvogadoCurrentSerializer(data=serializerData)
    serializer.is_valid()
    return Response(data=serializer.data)
