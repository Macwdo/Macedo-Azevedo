from datetime import date

from django.db.models import Q
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Cliente, ParteADV
from .serializers import ClienteSerializer, ParteADVSerializer


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        q = self.request.query_params.get("q", None)
        date_selected = self.request.query_params.get("iniciado", None)
        tipo = self.request.query_params.get("tipo", None)

        if q is None:
            q = ""

        date_qs, tipo_qs = "", ""

        if tipo is not None and tipo != "":
            try:
                tipo_qs = f"""Cliente.objects.filter(
                    Q(nome__istartswith=q) |
                    Q(email__istartswith=q) |
                    Q(cpf_cnpj__istartswith=q) |
                    Q(numero__istartswith=q) 
                    ) & Cliente.objects.filter(tipo="{tipo}")"""
            except:
                raise NotFound()

        if date_selected is not None and date_selected != "":
            date_selected = date_selected.split("/")
            if tipo_qs == "":
                date_qs = f"""Cliente.objects.filter(
                registro__gte="{date(int(date_selected[1]), int(date_selected[0]), 1)}",
                )"""
            else: 
                date_qs = f""" & Cliente.objects.filter(
                registro__gte="{date(int(date_selected[1]), int(date_selected[0]), 1)}",
                )"""
                
        if tipo_qs == "" and date_qs == "":
            qs = Cliente.objects.filter(
                    Q(nome__istartswith=q) |
                    Q(email__istartswith=q) |
                    Q(cpf_cnpj__istartswith=q) |
                    Q(numero__istartswith=q)
                    )
        elif tipo_qs == "" and date_qs != "":
            qs = Cliente.objects.filter(
                        Q(codigo_processo__istartswith=q) |
                        Q(parte_adversa__nome__istartswith=q)|
                        Q(advogado_responsavel__nome__istartswith=q)|
                        Q(cliente__nome__istartswith=q)|
                        Q(municipio__istartswith=q)|
                        Q(vara__istartswith=q)
                ) and eval(date_qs)

        elif tipo != "" and date_qs == "":
            qs = eval(tipo_qs)

        elif tipo == "" and date_qs != "":
            qs = eval(date_qs)
        
        else: 
            qs = eval(tipo_qs + date_qs)
            
        return qs.order_by("-id")


class ParteADVViewSet(ModelViewSet):
    queryset = ParteADV.objects.all()
    serializer_class = ParteADVSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        q = self.request.query_params.get("q", None)
        date_selected = self.request.query_params.get("iniciado", None)
        tipo = self.request.query_params.get("tipo", None)

        if q is None:
            q = ""


        date_qs, tipo_qs = "", ""

        if tipo is not None and tipo != "":
            try:
                tipo_qs = f"""ParteADV.objects.filter(
                    Q(nome__istartswith=q) |
                    Q(email__istartswith=q) |
                    Q(cpf_cnpj__istartswith=q) |
                    Q(numero__istartswith=q)
                    ) & ParteADV.objects.filter(tipo="{tipo}")"""
            except:
                raise NotFound()

        if date_selected is not None and date_selected != "":
            date_selected = date_selected.split("/")
            if tipo_qs == "":
                date_qs = f"""ParteADV.objects.filter(
                registro__gte="{date(int(date_selected[1]), int(date_selected[0]), 1)}",
                )"""
            else: 
                date_qs = f""" & ParteADV.objects.filter(
                registro__gte="{date(int(date_selected[1]), int(date_selected[0]), 1)}",
                )"""
        if tipo_qs == "" and date_qs == "":
            qs = ParteADV.objects.filter(
                    Q(nome__istartswith=q) |
                    Q(email__istartswith=q) |
                    Q(cpf_cnpj__istartswith=q) |
                    Q(numero__istartswith=q)
                    )
        elif tipo_qs == "" and date_qs != "":
            qs = ParteADV.objects.filter(
                        Q(codigo_processo__istartswith=q) |
                        Q(parte_adversa__nome__istartswith=q)|
                        Q(advogado_responsavel__nome__istartswith=q)|
                        Q(cliente__nome__istartswith=q)|
                        Q(municipio__istartswith=q)|
                        Q(vara__istartswith=q)
                ) and eval(date_qs)

        elif tipo != "" and date_qs == "":
            qs = eval(tipo_qs)

        elif tipo == "" and date_qs != "":
            qs = eval(date_qs)
        
        else: 
            qs = eval(tipo_qs + date_qs)

        return qs.order_by("-id")

