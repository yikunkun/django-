from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.shortcuts import HttpResponse
import re


class Rbac(MiddlewareMixin):

    def process_request(self, request):
        current_url = request.path_info
        permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)
        for i in settings.WHITE_URL_LIST:
            if re.match(i,current_url):
                return
        for item in permission_list:
            url = item.get('url')
            if re.match('^{}$'.format(url),current_url):
                return
        else:
            return HttpResponse('你没有该权限')

