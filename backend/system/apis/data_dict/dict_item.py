# -*- coding: utf-8 -*-
# @Time    : 2022/6/07 00:56
# @Author  : 臧成龙
# @FileName: dict_item.py
# @Software: PyCharm
from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema, Query, Schema, Field
from ninja.pagination import paginate
from system.models import DictItem
from utils.fu_crud import create, delete, update, retrieve
from utils.fu_ninga import MyPagination, FuFilters

router = Router()


class Filters(FuFilters):
    label: str = Field(None, alias="label")
    value: str = Field(None, alias="value")
    dict_id: str = Field(None, alias="dict_id")


class SchemaIn(ModelSchema):
    dict_id: int = Field(None, alias="dict_id")

    class Config:
        model = DictItem
        model_fields = ['label', 'value', 'sort', 'status']


class SchemaOut(ModelSchema):
    class Config:
        model = DictItem
        model_fields = ['id', 'label', 'value', 'sort', 'status']


@router.post("/dict_item", response=SchemaOut)
def create_dict_item(request, data: SchemaIn):
    qs = create(request, data, DictItem)
    return qs


@router.delete("/dict_item/{dict_item_id}")
def delete_dict_item(request, dict_item_id: int):
    delete(dict_item_id, DictItem)
    return {"success": True}


@router.put("/dict_item/{dict_item_id}", response=SchemaOut)
def update_dict_item(request, dict_item_id: int, data: SchemaIn):
    qs = update(request, dict_item_id, data, DictItem)
    return qs


@router.get("/dict_item", response=List[SchemaOut])
@paginate(MyPagination)
def list_dict_item(request, filters: Filters = Query(...)):
    qs = retrieve(request, DictItem, filters)
    return qs


@router.get("/dict_item/{dict_item_id}", response=SchemaOut)
def get_dict_item(request, dict_item_id: int):
    qs = get_object_or_404(DictItem, id=dict_item_id)
    return qs


@router.get("/dict_item/all/list", response=List[SchemaOut])
def all_list_role(request):
    qs = retrieve(request, DictItem)
    return qs
