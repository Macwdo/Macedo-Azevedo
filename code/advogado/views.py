from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.decorators import api_view
from celery import shared_task

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
def getCurrentUser(request: Request):
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

@shared_task()
@api_view(["GET"])
def sendEmail(request: Request):
    html_content = render_to_string("./emails/cliente_message.html", {
        "titulo":"Feliz Natal",
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
    
    email.attach_alternative(content=html_content,mimetype="text/html")
    email.send()
    return Response(data={"re": 'asd'})