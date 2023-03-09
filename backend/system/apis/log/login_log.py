# -*- coding: utf-8 -*-
# @Time    : 2022/6/07 00:56
# @Author  : 臧成龙
# @FileName: login_log.py
# @Software: PyCharm
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Field, ModelSchema, Query, Router, Schema
from ninja.pagination import paginate
from system.models import LoginLog
from utils.fu_crud import create, delete, retrieve, update
from utils.fu_ninja import FuFilters, MyPagination

router = Router()


class Filters(FuFilters):
    name: str = Field(None, alias="name")
    code: str = Field(None, alias="code")
    id: str = Field(None, alias="login_log_id")


class SchemaOut(ModelSchema):
    class Config:
        model = LoginLog
        model_fields = "__all__"


@router.delete("/login_log/{login_log_id}")
def delete_login_log(request, login_log_id: int):
    delete(login_log_id, LoginLog)
    return {"success": True}


@router.get("/login_log", response=List[SchemaOut])
@paginate(MyPagination)
def list_login_log(request, filters: Filters = Query(...)):
    qs = retrieve(request, LoginLog, filters)
    return qs


@router.get("/login_log/all/list", response=List[SchemaOut])
def all_list_role(request):
    qs = retrieve(request, LoginLog)
    return qs
