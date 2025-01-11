from django import template

register = template.Library()

@register.filter
def pluck(objects, attr):
    """Extracts a list of attribute values from a list of objects."""
    return [getattr(obj, attr) for obj in objects]
