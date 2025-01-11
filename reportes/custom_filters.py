from django import template

register = template.Library()

@register.filter
def pluck(objects, attr):
    return [getattr(obj, attr) for obj in objects]
