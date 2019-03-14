from django.conf import settings


# 把权限写进session中
def init_permission(request, user):
    permissions_query = user.roles.filter(permissions__url__isnull=False).values(
        'permissions__url',
        'permissions__is_menu',
        'permissions__icon',
        'permissions__title').distinct()
    permissions_list = []
    menus_list = []
    for item in permissions_query:
        permissions_list.append({'url': item['permissions__url']})
        if item['permissions__is_menu']:
            # 如果是菜单
            menus_list.append(
                {'icon': item['permissions__icon'],
                 'title': item['permissions__title'],
                 'url': item['permissions__url']
                 })
    # 将权限写进session中
    request.session[settings.PERMISSION_SESSION_KEY] = permissions_list
    # 将菜单写进session中
    request.session[settings.MENUS_SESSION_KEY] = menus_list
