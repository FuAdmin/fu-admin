# from application.ninja_cof import api
# Author 臧成龙
# coding=utf-8
# @Time    : 2022/5/15 21:47
# @File    : category_dict.py
# @Software: PyCharm
# @qq: 939589097

from typing import List

from django.shortcuts import get_object_or_404
from ninja import Field, ModelSchema, Query, Router, Schema
from ninja.pagination import paginate
from system.models import CategoryDict
from utils.fu_crud import create, delete, retrieve, update
from utils.fu_ninja import FuFilters, MyPagination
from utils.fu_response import FuResponse
from utils.list_to_tree import list_to_tree

router = Router()


class Filters(FuFilters):
    label: str = Field(None, alias="label")
    value: str = Field(None, alias="value")
    code: str = Field(None, alias="code")


class SchemaIn(ModelSchema):
    parent_id: int = None

    class Config:
        model = CategoryDict
        model_exclude = ['id', 'parent', 'create_datetime', 'update_datetime']


class SchemaOut(ModelSchema):
    class Config:
        model = CategoryDict
        model_fields = "__all__"
    # model_fields = []


@router.post("/category_dict", response=SchemaOut)
def create_category_dict(request, data: SchemaIn):
    category_dict = create(request, data, CategoryDict)
    return category_dict


@router.delete("/category_dict/{category_dict_id}")
def delete_category_dict(request, category_dict_id: int):
    delete(category_dict_id, CategoryDict)
    return {"success": True}


@router.put("/category_dict/{category_dict_id}", response=SchemaOut)
def update_category_dict(request, category_dict_id: int, data: SchemaIn):
    category_dict = update(request, category_dict_id, data, CategoryDict)
    return category_dict


@router.get("/category_dict", response=List[SchemaOut])
@paginate(MyPagination)
def list_category_dict(request, filters: Filters = Query(...)):
    qs = retrieve(request, CategoryDict, filters)
    return qs


@router.get("/category_dict/{category_dict_id}", response=SchemaOut)
def get_category_dict(request, category_dict_id: int):
    category_dict = get_object_or_404(CategoryDict, id=category_dict_id)
    return category_dict


@router.get("/category_dict/list/tree")
def list_category_dict_tree(request, filters: Filters = Query(...)):
    qs = retrieve(request, CategoryDict, filters).values()
    category_dict_tree = list_to_tree(list(qs))
    return FuResponse(data=category_dict_tree)
