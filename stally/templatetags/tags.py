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


@register.inclusion_tag('stally/campaigns_list_items.html')
def campaigns_list_items():
    from stally.models import Campaign
    campaigns = Campaign.objects.all()
    return {'campaigns': campaigns}
