from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django_rest_passwordreset.signals import reset_password_token_created


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = f"localhost:3000/recuperar-senha/?token={reset_password_token.key}"
    
    html_content = render_to_string("./emails/recuperar_senha.html", {
        "nome": reset_password_token.user.email,
        "url": email_plaintext_message
        })
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        "Recuperar sua senha",
        text_content,
        settings.EMAIL_HOST_USER,
        [reset_password_token.user.email]
    )

    email.attach_alternative(content=html_content,mimetype="text/html")
    email.send()