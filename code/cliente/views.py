from datetime import date

from django.db.models import Q
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from celery import shared_task
from cliente.models import Cliente, ParteADV, ClienteEndereco, ParteADVEndereco
from .serializers import ClienteSerializer, ParteADVSerializer, ClienteEnderecoSerializer, ParteADVEnderecoSerializer


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        q = self.request.query_params.get("q", None)
        tipo = self.request.query_params.get("tipo", None)

        client_qs = Cliente.objects.all()

        if q:
            client_qs = client_qs.filter(
                Q(nome__icontains=q) |
                Q(email__icontains=q) |
                Q(numero__icontains=q) |
                Q(cpf_cnpj__icontains=q) |
                Q(endereco__icontains=q) 
            )

        if tipo:
            client_qs = client_qs.filter(tipo=tipo)

        return client_qs.order_by("-id")


class ParteADVViewSet(ModelViewSet):
    queryset = ParteADV.objects.all()
    serializer_class = ParteADVSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        q = self.request.query_params.get("q", None)
        tipo = self.request.query_params.get("tipo", None)

        adverse_part_qs = ParteADV.objects.all()

        if q:
            adverse_part_qs = adverse_part_qs.filter(
                Q(nome__icontains=q) |
                Q(email__icontains=q) |
                Q(numero__icontains=q) |
                Q(cpf_cnpj__icontains=q) |
                Q(endereco__icontains=q) 
            )

        if tipo:
            adverse_part_qs = adverse_part_qs.filter(tipo=tipo)


        return adverse_part_qs.order_by("-id")


class ClienteEnderecoViewSet(ModelViewSet):
    queryset = ClienteEndereco.objects.all()
    serializer_class = ClienteEnderecoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cliente_pk = int(self.kwargs.get("cliente_pk"))
        try:
            cliente = Cliente.objects.get(pk=cliente_pk)
        except Cliente.DoesNotExist:
            raise NotFound()
        return self.queryset.filter(pk=cliente_pk)


class ParteADVEnderecoViewSet(ModelViewSet):
    queryset = ParteADVEndereco.objects.all()
    serializer_class = ParteADVEnderecoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        parteadv_pk = int(self.kwargs.get("parteadv_pk"))
        try:
            parteadv = ParteADV.objects.get(pk=parteadv_pk)
        except Cliente.DoesNotExist:
            raise NotFound()
        return self.queryset.filter(pk=parteadv_pk)


@shared_task()
@api_view(["GET"])
def sendEmail(request: Request):
    html_content = render_to_string("./emails/cliente_message.html", {
        "titulo": "Feliz Natal",
        "nome": "Daniel Macedo",
        "texto": "Uma mensagem de feliz natal"
    })
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        "Enviar Email",
        text_content,
        settings.EMAIL_HOST_USER,
        ["danilo.macedofernandes@hotmail.com"]
    )

    email.attach_alternative(content=html_content, mimetype="text/html")
    email.send()
    return Response(data={"re": 'asd'})
