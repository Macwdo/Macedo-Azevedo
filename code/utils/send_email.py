from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_email_with_template(registry_name, destiny, context):
    html_content = render_to_string("emails/cliente_message.html", context)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(f"Olá {registry_name}", text_content, settings.EMAIL_HOST_USER, [destiny])
    email.attach_alternative(html_content, 'text/html')
    email.send()