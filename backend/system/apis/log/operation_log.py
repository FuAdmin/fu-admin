# -*- coding: utf-8 -*-
# @Time    : 2022/6/07 00:56
# @Author  : 臧成龙
# @FileName: operation_log.py
# @Software: PyCharm
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Field, ModelSchema, Query, Router, Schema
from ninja.pagination import paginate
from system.models import OperationLog
from utils.fu_crud import create, delete, retrieve, update
from utils.fu_ninja import FuFilters, MyPagination

router = Router()


class Filters(FuFilters):
    request_username: str = Field(None, alias="request_username")
    id: str = Field(None, alias="operation_log_id")


class SchemaOut(ModelSchema):
    class Config:
        model = OperationLog
        model_fields = "__all__"


@router.delete("/operation_log/{operation_log_id}")
def delete_operation_log(request, operation_log_id: int):
    delete(operation_log_id, OperationLog)
    return {"success": True}


@router.get("/operation_log", response=List[SchemaOut])
@paginate(MyPagination)
def list_operation_log(request, filters: Filters = Query(...)):
    qs = retrieve(request, OperationLog, filters)
    return qs


@router.get("/operation_log/all/list", response=List[SchemaOut])
def all_list_role(request):
    qs = retrieve(request, OperationLog)
    return qs
