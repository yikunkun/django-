import re
from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('rabc/menu.html')
def menus(request):
    menus_list = request.session.get(settings.MENUS_SESSION_KEY)
    for item in menus_list:
        # 如果当前的url和菜单中的url匹配上
        if re.match(item.get('url'),request.path_info):
            item['class'] = 'active'

    return {'menus_list':menus_list}