from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

# Create your views here.


@api_view(["GET"])
def sendEmail(request: Request):
    html_content = render_to_string("./emails/cliente_message.html", {
        "titulo":"Feliz Natal",
        "nome": "Danilo Macedo",
        "texto": "Uma mensagem de feliz natal"
    })
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        "Enviar Email",
        text_content,
        settings.EMAIL_HOST_USER,
        [""]
    )

    email.attach_alternative(content=html_content,mimetype="text/html")
    email.send()
    return Response(data={"REc": "per"})