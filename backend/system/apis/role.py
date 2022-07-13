# from application.ninja_cof import api
# Author 臧成龙
# coding=utf-8
# @Time    : 2022/5/19 21:36
# @File    : role.py
# @Software: PyCharm
# @qq: 939589097

from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Schema, Field
from ninja.pagination import paginate
from system.models import Role, Menu
from utils.fu_crud import create, delete, retrieve

from utils.fu_ninga import MyPagination, FuFilters

router = Router()


class Filters(FuFilters):
    name: str = Field(None, alias="name")
    status: bool = Field(None, alias="status")
    id: str = Field(None, alias="id")


class SchemaIn(ModelSchema):
    menu: list = []
    permission: list = []
    dept: list = []

    class Config:
        model = Role
        model_exclude = ['id', 'dept', 'menu', 'permission', 'create_datetime', 'update_datetime']


class SchemaOut(ModelSchema):
    class Config:
        model = Role
        model_fields = "__all__"
    # model_fields = []


@router.post("/role", response=SchemaOut)
def create_role(request, data: SchemaIn):
    dict_data = data.dict()
    del dict_data['menu']
    del dict_data['permission']
    del dict_data['dept']
    role = create(request, dict_data, Role)
    return role


@router.delete("/role/{role_id}")
def delete_role(request, role_id: int):
    delete(role_id, Role)
    return {"success": True}


@router.put("/role/{role_id}", response=SchemaOut)
def update_role(request, role_id: int, payload: SchemaIn):
    post = get_object_or_404(Role, id=role_id)
    for attr, value in payload.dict().items():
        if attr == 'menu':
            post.menu.set(value)
        elif attr == 'permission':
            post.permission.set(value)
        elif attr == 'dept':
            post.dept.set(value)
        else:
            setattr(post, attr, value)
    post.save()
    return post


@router.get("/role", response=List[SchemaOut])
@paginate(MyPagination)
def list_role(request, filters: Filters = Query(...)):
    qs = retrieve(request, Role, filters)
    return qs


@router.get("/role/all/list", response=List[SchemaOut])
def all_list_role(request):
    qs = retrieve(request, Role)
    return qs


@router.get("/role/{role_id}", response=SchemaOut)
def get_role(request, role_id: int):
    role = get_object_or_404(Role, id=role_id)
    return role


@router.get("/role/list/menu_button")
def list_menu_button_tree(request):
    qs = Menu.objects.all()
    result = []
    for item in qs:
        dict_item = item.__dict__
        menu_button = list(item.menuPermission.all().values())
        for button_item in menu_button:
            button_item['id'] = f"b{button_item['id']}"
            button_item['parent_id'] = button_item.pop('menu_id')
            button_item['title'] = button_item.pop('name')

        # dict_item['menu_button'] = list(item.menuPermission.all().values())
        del dict_item['_state']
        result.append(dict_item)
        result.extend(menu_button)

    return result
