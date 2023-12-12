from django import template

from processo.forms import LawsuitFileForm, LawsuitValuesForm
from registry.forms import (
    RegistryAddressForm,
    RegistryCnpjForm,
    RegistryContactForm,
    RegistryCpfForm,
    RegistryForm,
)

register = template.Library()

@register.filter('form_instanced')
def form_instanced(form, model):
    eval_form_string = f"{form.__class__.__name__}(instance=model)"
    form_instanced = eval(eval_form_string)
    return form_instanced
