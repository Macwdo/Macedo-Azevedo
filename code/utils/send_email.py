from io import BytesIO
from mimetypes import guess_type
from smtplib import SMTPAuthenticationError, SMTPSenderRefused
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.text import slugify
from django.contrib import messages
import sentry_sdk


@shared_task
def send_email_with_template(registry_name, destiny, context, files):
    html_content = render_to_string("emails/cliente_message.html", context)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        f"Olá {registry_name}",
        text_content, settings.EMAIL_HOST_USER,
        [destiny]
        )
    email.attach_alternative(html_content, 'text/html')
    for file in files:
        file_content = BytesIO(file.read())
        content_type, encoding = guess_type(file.name)
        content_type = content_type or 'application/octet-stream'

        email.attach(
            filename=slugify(file.name),
            content=file_content.getvalue(),
            mimetype=content_type
        )
        
    email.send()


