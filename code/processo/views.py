from advogado.models import Advogado
from processo.serializers import ProcessosAnexosSerializer, ProcessosSerializer, ProcessosHonorariosSerializer, ProcessosAssuntosSerializer
from datetime import date
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from processo.models import Processos, ProcessosHonorarios, ProcessosAnexos, ProcessosAssuntos, ProcessoMovimento
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from processo.tasks import track_process


class ProcessosViewSet(ModelViewSet):
    queryset = Processos.objects.all()
    serializer_class = ProcessosSerializer
    permission_classes = [IsAuthenticated]

    
    def finalize_response(self, request, response, *args, **kwargs):
        # if response.status_code == 201:
        #     track_process.delay(response.data["codigo_processo"], response.data["id"])

        return super().finalize_response(request, response, *args, **kwargs)

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


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def finalizar_processo(request, id):
    processo = get_object_or_404(Processos, pk=id)
    if processo.finalizado == None:
        processo.finalizado = datetime.now()
        processo.save()
        serializer = ProcessosSerializer(processo, many=False)
        return Response(data=serializer.data)
    else:
        return Response(data={"detail": "este processo ja foi finalizado"}, status=status.HTTP_400_BAD_REQUEST)


class ProcessosHonorariosViewSet(ModelViewSet):
    queryset = ProcessosHonorarios.objects.all()
    serializer_class = ProcessosHonorariosSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.validated_data["processo_id"] = self.kwargs["processo_pk"]
        return super().perform_create(serializer)

    def get_queryset(self, *args, **kwargs):
        processo_pk = int(self.kwargs.get("processo_pk"))
        try:
            processo = Processos.objects.get(pk=processo_pk)
        except Processos.DoesNotExist:
            raise NotFound()
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
        try:
            processo = Processos.objects.get(pk=processo_pk)
        except Processos.DoesNotExist:
            raise NotFound()
        return self.queryset.filter(processo=processo_pk)


class ProcessosAssuntosViewSet(ModelViewSet):
    queryset = ProcessosAssuntos.objects.all()
    serializer_class = ProcessosAssuntosSerializer
    permission_classes = [IsAuthenticated]

