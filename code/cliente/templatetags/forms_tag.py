from django import template
from cliente.forms import ClientAddressForm, ClientContactForm, ClientForm

register = template.Library()

@register.filter('form_instanced_client')
def form_instanced(form, model):
    eval_form_string = f"{form.__class__.__name__}(instance=model)"
    form_instanced = eval(eval_form_string)
    return form_instanced