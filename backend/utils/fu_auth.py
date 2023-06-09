# -*- coding: utf-8 -*-
# @Time    : 2022/6/2 23:19
# @Author  : 臧成龙
# @FileName: fu_auth.py
# @Software: PyCharm
# -*- coding: utf-8 -*-

import re
from datetime import datetime

# from django.core.cache import cache
from fuadmin.settings import DEMO, SECRET_KEY, WHITE_LIST
from ninja.security import HttpBearer
from system.models import MenuButton, Users

from .fu_jwt import FuJwt
from .fu_ninja import FuFilters
from .usual import get_dept, get_user_info_from_token

METHOD = {
    'GET': 0,
    'POST': 1,
    'PUT': 2,
    'DELETE': 3,
}


class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        jwt = FuJwt(SECRET_KEY)
        value = jwt.decode(SECRET_KEY, token)
        time_now = int(datetime.now().timestamp())
        # 判断token是否过期
        if value.valid_to >= time_now:
            token_user = value.payload
            token_user_id = token_user['id']
            user = Users.objects.get(id=token_user_id)
            request_path = request.path
            request_method = request.method
            if DEMO:
                # 判断是否在白名单中
                if request_path in WHITE_LIST:
                    return token
                if request_method == 'GET':
                    return token
                else:
                    raise TimeoutError(403, '演示环境')
            else:
                # 判断是否是超级管理员
                if not token_user['is_superuser']:
                    # 判断是path是否是‘/数字’结尾
                    result = re.search(r'/\d+$', request_path)
                    if result:
                        match_value = result.group()
                        # 将数字结尾的接口替换成.*? 因为接口中是/{id}
                        request_path = request_path.replace(match_value, '/*')
                    # 判断是否在白名单中
                    if request_path in WHITE_LIST:
                        return token
                    else:
                        menuIds = user.role.values_list('permission__id', flat=True)
                        queryset = MenuButton.objects.filter(id__in=menuIds, api__regex=request_path,
                                                             method=METHOD[request_method])
                        if queryset.exists():
                            return token
                        else:
                            raise TimeoutError(403, '没有权限')
            # cache_token = cache.get(token_user_id)
            # if token == cache_token:
            return token
        else:
            raise TimeoutError(401, 'token时间过期')


def data_permission(request, filters: FuFilters):
    user_info = get_user_info_from_token(request)
    if user_info['is_superuser']:
        return filters
    user = Users.objects.get(id=user_info['id'])
    data_range_qs = user.role.values_list('data_range', flat=True)
    dept_ids = user.role.values_list('dept__id', flat=True)

    # 如果有多个角色，取数据权限最大的角色
    data_range = max(list(data_range_qs))

    # 仅本人数据权限
    if data_range == 0:
        filters.creator_id = user_info['id']

    # 本部门数据权限
    if data_range == 1:
        filters.belong_dept = user_info['dept']

    # 本部门及以下数据权限
    if data_range == 2:
        dept_and_below_ids = get_dept(user_info['dept'])
        filters.belong_dept__in = dept_and_below_ids

    # 自定义数据权限
    if data_range == 3:
        filters.belong_dept__in = list(dept_ids)

    # 所有数据权限
    if data_range == 4:
        pass

    return filters



