
from django import template
from django import forms

register = template.Library()


@register.filter
def is_radio(field):
    return isinstance(field.field.widget, forms.RadioSelect)
