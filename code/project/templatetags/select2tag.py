from django import template
from cliente.forms import ClientAddressForm, ClientContactForm, ClientForm
from parte_adversa.forms import AdversePartAddressForm, AdversePartContactForm, AdversePartForm
from processo.forms import LawsuitFileForm, LawsuitValuesForm

register = template.Library()

@register.filter('is_select2')
def is_select2(field):
    field_string = str(field)
    return True if "select2" in field_string else False
