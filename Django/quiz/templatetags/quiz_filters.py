from django import template

register = template.Library()


@register.filter(name="accessList")
def accessList(value, position):
    answer = value[int(position)]
    return answer