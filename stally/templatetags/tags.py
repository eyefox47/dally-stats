from django import template
register = template.Library()

@register.simple_tag
def active(request, pattern):
    import re
    if pattern == '/':
        if request.path == '/':
            return 'active'
        else:
            return ''

    if re.search(pattern, request.path):
        return 'active'
    return ''
