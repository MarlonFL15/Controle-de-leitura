from django import template
from django.utils.safestring import mark_safe
import json
register = template.Library()

@register.filter(name='addClass')
def addClass(value, arg):
    return value.as_widget(attrs={'class':arg})

@register.filter(is_safe=True)
def js(obj):
    return mark_safe(json.dumps(obj))