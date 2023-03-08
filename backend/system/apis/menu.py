# Author 臧成龙
# coding=utf-8
# @Time    : 2022/5/15 21:47
# @File    : menu.py
# @Software: PyCharm
# @qq: 939589097

from typing import List

from django.shortcuts import get_object_or_404
from fuadmin.settings import SECRET_KEY
from ninja import Field, ModelSchema, Query, Router, Schema
from ninja.pagination import paginate
from system.models import Menu, MenuButton, Users
from utils.fu_crud import create, delete, retrieve, update
from utils.fu_jwt import FuJwt
from utils.fu_ninja import FuFilters, MyPagination
from utils.fu_response import FuResponse
from utils.list_to_tree import list_to_route, list_to_tree

router = Router()


class Filters(FuFilters):
    title: str = Field(None, alias="title")
    status: bool = Field(None, alias="status")
    id: str = Field(None, alias="id")


class SchemaIn(ModelSchema):
    parent_id: int = None
    component: str = 'LAYOUT'

    class Config:
        model = Menu
        model_exclude = ['id', 'parent', 'create_datetime', 'update_datetime']


class SchemaOut(ModelSchema):
    class Config:
        model = Menu
        model_fields = "__all__"
    # model_fields = []


@router.post("/menu", response=SchemaOut)
def create_menu(request, data: SchemaIn):
    menu = create(request, data, Menu)
    return menu


@router.delete("/menu/{menu_id}")
def delete_menu(request, menu_id: int):
    delete(menu_id, Menu)
    return {"success": True}


@router.put("/menu/{menu_id}", response=SchemaOut)
def update_menu(request, menu_id: int, data: SchemaIn):
    post = update(request, menu_id, data, Menu)
    return post


@router.get("/menu", response=List[SchemaOut])
def list_menu_tree(request, filters: Filters = Query(...)):
    qs = retrieve(request, Menu, filters).values()
    # 将查询集转换成树形结构
    menu_tree = list_to_tree(list(qs))
    return FuResponse(data=menu_tree)


@router.get("/menu/{menu_id}", response=SchemaOut)
def get_menu(request, menu_id: int):
    post = get_object_or_404(Menu, id=menu_id)
    return post


@router.get("/menu/route/tree")
def route_menu_tree(request):
    """用于前端获取当前角色的路由"""
    token = request.META.get("HTTP_AUTHORIZATION")
    token = token.split(" ")[1]
    token_user = FuJwt(SECRET_KEY).decode(SECRET_KEY, token).payload
    user = Users.objects.get(id=token_user['id'])
    queryset = Menu.objects.filter(status=1).values()
    if not token_user['is_superuser']:
        menuIds = user.role.values_list('menu__id', flat=True)
        queryset = Menu.objects.filter(id__in=menuIds, status=1).values()
    menu_tree = list_to_route(list(queryset))
    return FuResponse(data=menu_tree)

