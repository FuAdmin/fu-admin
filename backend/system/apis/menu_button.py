# Author 臧成龙
# coding=utf-8
# @Time    : 2022/5/21 21:26
# @File    : menu_menu_button.py
# @Software: PyCharm
# @qq: 939589097

from typing import List

from django.shortcuts import get_object_or_404
from ninja import Field, ModelSchema, Query, Router, Schema
from ninja.pagination import paginate
from system.models import MenuButton
from utils.fu_crud import create, delete, retrieve, update
from utils.fu_ninja import FuFilters, MyPagination

router = Router()


class Filters(FuFilters):
    name: str = Field(None, alias="name")
    code: str = Field(None, alias="code")
    menu_id: str = Field(None, alias="menu_id")


class SchemaIn(ModelSchema):
    menu_id: int = None

    class Config:
        model = MenuButton
        model_exclude = ['id', 'menu', 'create_datetime', 'update_datetime']


class SchemaOut(ModelSchema):
    class Config:
        model = MenuButton
        model_fields = "__all__"
    # model_fields = []


@router.post("/menu_button", response=SchemaOut)
def create_menu_button(request, data: SchemaIn):
    menu_button = create(request, data, MenuButton)
    return menu_button


@router.delete("/menu_button/{menu_button_id}")
def delete_menu_button(request, menu_button_id: int):
    delete(menu_button_id, MenuButton)
    return {"success": True}


@router.put("/menu_button/{menu_button_id}", response=SchemaOut)
def update_menu_button(request, menu_button_id: int, data: SchemaIn):
    menu_button = update(request, menu_button_id, data, MenuButton)
    return menu_button


@router.get("/menu_button", response=List[SchemaOut])
@paginate(MyPagination)
def list_menu_button(request, filters: Filters = Query(...)):
    qs = retrieve(request, MenuButton, filters)
    return qs


@router.get("/menu_button/{menu_button_id}", response=SchemaOut)
def get_menu_button(request, menu_button_id: int):
    post = get_object_or_404(MenuButton, id=menu_button_id)
    return post
