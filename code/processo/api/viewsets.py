from .serializers import (
    ProcessosAnexosSerializer, ProcessosSerializer,
    ProcessosHonorariosSerializer, ProcessosAssuntosSerializer,
    ProcessosMovimentoSerializer
)
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from processo.models import Processos, ProcessosHonorarios, ProcessosAnexos, ProcessosAssuntos, ProcessosMovimento
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action


class ProcessosViewSet(ModelViewSet):
    queryset = Processos.objects.all()
    serializer_class = ProcessosSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["GET"])
    def finalizar(self, request, pk):
        processo = get_object_or_404(Processos, pk=pk)
        if not processo.finalizado:
            processo.finalizado = datetime.now()
            processo.save()
            serializer = ProcessosSerializer(processo, many=False)
            return Response(data=serializer.data)
        else:
            return Response(data={"detail": "este processo ja foi finalizado"}, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        q = self.request.query_params.get("q", None)
        laywer = self.request.query_params.get("advogado", None)
        finished = self.request.query_params.get("finalizado", None)
        lawsuits = Processos.objects.all()

        if q:
            lawsuits = lawsuits.filter(
                Q(codigo_processo__icontains=q) |
                Q(posicao__icontains=q) |
                Q(observacoes__icontains=q) |
                Q(estado__icontains=q) |
                Q(municipio__icontains=q) |
                Q(assunto__icontains=q) |
                Q(vara__icontains=q) |
                Q(n_vara__icontains=q) |
                Q(advogado_responsavel__nome__icontains=q) |
                Q(advogado_responsavel__email__icontains=q) |
                Q(advogado_responsavel__oab__icontains=q) |
                Q(colaborador__nome__icontains=q) |
                Q(colaborador__email__icontains=q) |
                Q(colaborador__oab__icontains=q) |
                Q(parte_adversa__nome__icontains=q) |
                Q(parte_adversa__email__icontains=q) |
                Q(parte_adversa__numero__icontains=q) |
                Q(parte_adversa__cpf_cnpj__icontains=q) |
                Q(parte_adversa__endereco__icontains=q) |
                Q(cliente__nome__icontains=q) |
                Q(cliente__email__icontains=q) |
                Q(cliente__numero__icontains=q) |
                Q(cliente__cpf_cnpj__icontains=q) |
                Q(cliente__endereco__icontains=q) 
            )
        
        if laywer:
            lawsuits = lawsuits.filter(
                advogado_responsavel_id=laywer
            )

        if finished:
            if finished.upper() == "TRUE":
                lawsuits = lawsuits.exclude(finalizado__isnull=True)

        return lawsuits.order_by("-id")

    
class ProcessosHonorariosViewSet(ModelViewSet):
    queryset = ProcessosHonorarios.objects.all()
    serializer_class = ProcessosHonorariosSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.validated_data["processo_id"] = self.kwargs["processo_pk"]
        return super().perform_create(serializer)

    def get_queryset(self, *args, **kwargs):
        processo_pk = int(self.kwargs.get("processo_pk"))
        return self.queryset.filter(processo=processo_pk)


class ProcessosAnexosViewSet(ModelViewSet):
    queryset = ProcessosAnexos.objects.all()
    serializer_class = ProcessosAnexosSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.validated_data["processo_id"] = self.kwargs["processo_pk"]
        return super().perform_create(serializer)

    def get_queryset(self, *args, **kwargs):
        processo_pk = int(self.kwargs.get("processo_pk"))
        return self.queryset.filter(processo=processo_pk)


class ProcessosAssuntosViewSet(ModelViewSet):
    queryset = ProcessosAssuntos.objects.all()
    serializer_class = ProcessosAssuntosSerializer
    permission_classes = [IsAuthenticated]


class ProcessosMovimentoViewSet(ModelViewSet):
    queryset = ProcessosMovimento.objects.all()
    serializer_class = ProcessosMovimentoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.validated_data["processo_id"] = self.kwargs["processo_pk"]
        return super().perform_create(serializer)

    def get_queryset(self, *args, **kwargs):
        processo_pk = int(self.kwargs.get("processo_pk"))
        return self.queryset.filter(processo=processo_pk).order_by("-id")
