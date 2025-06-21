from urllib.parse import urlencode

from django import template

register = template.Library()

@register.simple_tag
def url_query_append(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()
