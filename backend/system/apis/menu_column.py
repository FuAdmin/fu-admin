# Author 臧成龙
# coding=utf-8
# @Time    : 2023/3/27 23:26
# @File    : menu_menu_column_field.py
# @Software: PyCharm
# @qq: 939589097

from typing import List

from django.shortcuts import get_object_or_404
from ninja import Field, ModelSchema, Query, Router, Schema
from ninja.pagination import paginate
from system.models import MenuColumnField
from utils.fu_crud import create, delete, retrieve, update, batch_create
from utils.fu_ninja import FuFilters, MyPagination
from utils.fu_response import FuResponse

router = Router()


class Filters(FuFilters):
    name: str = Field(None, alias="name")
    code: str = Field(None, alias="code")
    menu_id: str = Field(None, alias="menu_id")


class SchemaIn(ModelSchema):
    menu_id: str = Field(None, alias="menu_id")

    class Config:
        model = MenuColumnField
        model_exclude = ['id', 'menu', 'create_datetime', 'update_datetime']


class BatchSchemaIn(Schema):
    batch_info: list = Field(None, alias="batch_info")


class SchemaOut(ModelSchema):
    class Config:
        model = MenuColumnField
        model_fields = "__all__"
    # model_fields = []


@router.post("/menu_column_field", response=SchemaOut)
def create_menu_column_field(request, data: SchemaIn):
    menu_column_field = create(request, data, MenuColumnField)
    return menu_column_field


@router.post("/menu_column_field/batch/create")
def batch_create_menu_column_field(request, data: BatchSchemaIn):
    batch_create(request, data.batch_info, MenuColumnField)
    return FuResponse(msg="导入成功")


@router.delete("/menu_column_field/{menu_column_field_id}")
def delete_menu_column_field(request, menu_column_field_id: int):
    delete(menu_column_field_id, MenuColumnField)
    return {"success": True}


@router.put("/menu_column_field/{menu_column_field_id}", response=SchemaOut)
def update_menu_column_field(request, menu_column_field_id: int, data: SchemaIn):
    menu_column_field = update(request, menu_column_field_id, data, MenuColumnField)
    return menu_column_field


@router.get("/menu_column_field", response=List[SchemaOut])
@paginate(MyPagination)
def list_menu_column_field(request, filters: Filters = Query(...)):
    qs = retrieve(request, MenuColumnField, filters)
    return qs


@router.get("/menu_column_field/{menu_column_field_id}", response=SchemaOut)
def get_menu_column_field(request, menu_column_field_id: int):
    post = get_object_or_404(MenuColumnField, id=menu_column_field_id)
    return post
