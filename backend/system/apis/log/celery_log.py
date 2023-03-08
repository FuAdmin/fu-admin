# -*- coding: utf-8 -*-
# @Time    : 2022/6/14 23:
# @Author  : 臧成龙
# @FileName: celery_log.py
# @Software: PyCharm
from typing import List

from django_celery_results.models import TaskResult
from ninja import Field, ModelSchema, Query, Router, Schema
from ninja.pagination import paginate
from utils.fu_crud import delete, retrieve
from utils.fu_ninja import FuFilters, MyPagination

router = Router()


class Filters(FuFilters):
    periodic_task_name: str = Field(None, alias="periodic_task_name")


class SchemaOut(ModelSchema):
    class Config:
        model = TaskResult
        model_fields = "__all__"


@router.delete("/celery_log/{celery_log_id}")
def delete_celery_log(request, celery_log_id: int):
    delete(celery_log_id, TaskResult)
    return {"success": True}


@router.get("/celery_log", response=List[SchemaOut])
@paginate(MyPagination)
def list_celery_log(request, filters: Filters = Query(...)):
    qs = retrieve(request, TaskResult, filters)
    return qs


@router.get("/celery_log/all/list", response=List[SchemaOut])
def all_list_role(request):
    qs = retrieve(request, TaskResult)
    return qs
