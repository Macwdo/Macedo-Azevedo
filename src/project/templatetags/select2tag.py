from django import template

from processo.forms import LawsuitFileForm, LawsuitValuesForm
from registry.forms import (
    RegistryAddressForm,
    RegistryContactForm,
    RegistryForm,
)

register = template.Library()

@register.filter('is_select2')
def is_select2(field):
    field_string = str(field)
    return True if "select2" in field_string else False
