from django import template
register = template.Library()


@register.simple_tag
def active(request, pattern):
    import re
    if pattern == '/':
        if request.path == '/':
            return 'active-header-tab'
        else:
            return ''

    if re.search(pattern, request.path):
        return 'active-header-tab'
    return ''


@register.inclusion_tag('database/campaigns_list_items.html')
def campaigns_list_items():
    from apps.database.models import Campaign
    campaigns = Campaign.objects.all()
    return {'campaigns': campaigns}
