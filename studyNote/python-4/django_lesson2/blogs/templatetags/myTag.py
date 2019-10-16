
#固定引入格式
from django import template
from django.utils.safestring import mark_safe
register=template.Library() #register名字固定，不能改变

@register.filter
def filter_multi(x,y):
    return x*y


@register.simple_tag
def simple_tag_multi(x,y):

    return x*y