from django import template

register = template.Library()


@register.filter('is_select2')
def is_select2(field):
    field_string = str(field)
    return True if 'select2' in field_string else False
