from django import template
from registry.forms import RegistryForm, RegistryContactForm, RegistryAddressForm
from processo.forms import LawsuitFileForm, LawsuitValuesForm

register = template.Library()

@register.filter('is_select2')
def is_select2(field):
    field_string = str(field)
    return True if "select2" in field_string else False
