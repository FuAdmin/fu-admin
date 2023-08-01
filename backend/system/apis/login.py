# -*- coding: utf-8 -*-
# @Time    : 2022/5/14 15:05
# @Author  : 臧成龙
# @FileName: login.py
# @Software: PyCharm
import json
from datetime import datetime
# from django.core.cache import cache

from django.contrib import auth
from django.forms import model_to_dict
from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Schema, Field

from fuadmin.settings import SECRET_KEY, TOKEN_LIFETIME
from system.models import Users, Role, MenuButton, MenuColumnField
from utils.fu_jwt import FuJwt
from utils.fu_response import FuResponse
from utils.request_util import save_login_log
from utils.usual import get_user_info_from_token

router = Router()


class SchemaOut(ModelSchema):
    homePath: str = Field(None, alias="home_path")

    class Config:
        model = Users
        model_exclude = ['password', 'role', 'post']


class LoginSchema(Schema):
    username: str = Field(None, alias="username")
    password: str = Field(None, alias="password")


class Out(Schema):
    multi_depart: str
    sysAllDictItems: str
    departs: str
    userInfo: SchemaOut
    token: str


@router.post("/login", response=Out, auth=None)
def login(request, data: LoginSchema):
    user_obj = auth.authenticate(request, **data.dict())
    if user_obj:
        request.user = user_obj
        role = user_obj.role.all().values('id')
        post = list(user_obj.post.all().values('id'))
        role_list = []
        post_list = []
        for item in role:
            role_list.append(item['id'])
        for item in post:
            post_list.append(item['id'])
        user_obj_dic = model_to_dict(user_obj)
        user_obj_dic['post'] = post_list
        user_obj_dic['role'] = role_list
        del user_obj_dic['password']
        del user_obj_dic['avatar']

        time_now = int(datetime.now().timestamp())
        jwt = FuJwt(SECRET_KEY, user_obj_dic, valid_to=time_now + TOKEN_LIFETIME)
        # 将生成的token加入缓存
        # cache.set(user_obj.id, jwt.encode())
        token = f"bearer {jwt.encode()}"
        data = {
            "multi_depart": 1,
            "sysAllDictItems": "q",
            "departs": "e",
            'userInfo': user_obj_dic,
            'token': token
        }
        save_login_log(request=request)
        return data
    else:
        return FuResponse(code=500, msg="账号/密码错误")


@router.get("/logout", auth=None)
def get_post(request):
    # 删除缓存
    user_info = get_user_info_from_token(request)
    # cache.delete(user_info['id'])
    return FuResponse(msg="注销成功")


@router.get("/userinfo", response=SchemaOut)
def get_userinfo(request):
    user_info = get_user_info_from_token(request)
    user = get_object_or_404(Users, id=user_info['id'])
    return user


@router.get("/permCode")
def route_menu_tree(request):
    """用于前端获取当前用户的按钮权限"""
    token_user = get_user_info_from_token(request)
    user = Users.objects.get(id=token_user['id'])

    if not token_user['is_superuser']:
        menu_button_ids = user.role.values_list('permission__id', flat=True)
        menu_column_ids = user.role.values_list('column__id', flat=True)

        # queryset = MenuButton.objects.filter(id__in=menuIds, status=1).values()
        queryset_button = MenuButton.objects.filter(id__in=menu_button_ids)
        queryset_column = MenuColumnField.objects.filter(id__in=menu_column_ids)
    else:
        queryset_button = MenuButton.objects.all()
        queryset_column = MenuColumnField.objects.all()

    queryset = [*queryset_button, *queryset_column]
    code_list = []
    for item in queryset:
        code_list.append(item.code)
    return FuResponse(data=code_list)
