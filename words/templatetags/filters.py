from django import template

register = template.Library()


@register.filter
def percent(value: str, arg: str):
    value = str(value)
    arg = str(arg)

    if not value.isdigit() or not arg.isdigit():
        return value

    return int(100 * (int(value) - int(arg)) / int(value))
