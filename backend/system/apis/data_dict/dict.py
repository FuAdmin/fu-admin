# -*- coding: utf-8 -*-
# @Time    : 2022/6/07 00:56
# @Author  : 臧成龙
# @FileName: dict.py
# @Software: PyCharm
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Field, ModelSchema, Query, Router, Schema
from ninja.pagination import paginate
from system.models import Dict
from utils.fu_crud import create, delete, retrieve, update
from utils.fu_ninja import FuFilters, MyPagination

router = Router()


class Filters(FuFilters):
    name: str = Field(None, alias="name")
    status: bool = Field(None, alias="status")
    id: str = Field(None, alias="dict_id")


class SchemaIn(ModelSchema):
    class Config:
        model = Dict
        model_fields = ['name', 'code', 'sort', 'status']


class SchemaOut(ModelSchema):
    class Config:
        model = Dict
        model_fields = ['id', 'name', 'code', 'sort', 'status']


@router.post("/dict", response=SchemaOut)
def create_dict(request, data: SchemaIn):
    qs = create(request, data, Dict)
    return qs


@router.delete("/dict/{dict_id}")
def delete_dict(request, dict_id: int):
    delete(dict_id, Dict)
    return {"success": True}


@router.put("/dict/{dict_id}", response=SchemaOut)
def update_dict(request, dict_id: int, data: SchemaIn):
    qs = update(request, dict_id, data, Dict)
    return qs


@router.get("/dict", response=List[SchemaOut])
@paginate(MyPagination)
def list_dict(request, filters: Filters = Query(...)):
    qs = retrieve(request, Dict, filters)
    return qs


@router.get("/dict/{dict_id}", response=SchemaOut)
def get_dict(request, dict_id: int):
    qs = get_object_or_404(Dict, id=dict_id)
    return qs


@router.get("/dict/all/list", response=List[SchemaOut])
def all_list_role(request):
    qs = retrieve(request, Dict)
    return qs
