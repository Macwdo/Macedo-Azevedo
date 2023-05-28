from django import template
from cliente.forms import ClientAddressForm, ClientContactForm, ClientForm
from parte_adversa.forms import AdversePartAddressForm, AdversePartContactForm, AdversePartForm
from processo.forms import LawsuitFileForm, LawsuitValuesForm

register = template.Library()

@register.filter('form_instanced')
def form_instanced(form, model):
    eval_form_string = f"{form.__class__.__name__}(instance=model)"
    form_instanced = eval(eval_form_string)
    return form_instanced
