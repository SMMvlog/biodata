from django import template
register = template.Library()

@register.filter(name="rep")
def remove(value,arg):
    for char in arg:
        value = value.replace(char,"")
    return value