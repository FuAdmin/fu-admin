# -*- coding: utf-8 -*-
# @Time    : 2022/6/14 01:50
# @Author  : 臧成龙
# @FileName: periodic_task.py
# @Software: PyCharm
from typing import List

from django.forms import model_to_dict
from django.shortcuts import get_object_or_404
from django_celery_beat.models import CrontabSchedule, IntervalSchedule, PeriodicTask
from ninja import ModelSchema, Router, Schema
from ninja.pagination import paginate
from pydantic import Field
from system.apis import celery_crontab, celery_interval
from utils.fu_crud import create, delete, retrieve, update
from utils.fu_ninja import MyPagination
from utils.fu_response import FuResponse

router = Router()


class SchemaIn(ModelSchema):
    interval_id: int = Field(None, alias="interval")
    crontab_id: int = Field(None, alias="crontab")

    class Config:
        model = PeriodicTask
        model_fields = ['task', 'name', 'enabled']


class SchemaOut(ModelSchema):
    interval: celery_interval.SchemaOut = None
    crontab: celery_crontab.SchemaOut = None

    class Config:
        model = PeriodicTask
        model_fields = ['id', 'task', 'name', 'enabled']


@router.post("/periodic_task", response=SchemaOut)
def create_periodic_task(request, data: SchemaIn):
    qs = PeriodicTask.objects.create(**data.dict())
    return qs


@router.delete("/periodic_task/{periodic_task_id}")
def delete_periodic_task(request, periodic_task_id: int):
    delete(periodic_task_id, PeriodicTask)
    return {"success": True}


@router.put("/periodic_task/{periodic_task_id}", response=SchemaOut)
def update_periodic_task(request, periodic_task_id: int, data: SchemaIn):
    instance = get_object_or_404(PeriodicTask, id=periodic_task_id)
    for attr, value in data.dict().items():
        setattr(instance, attr, value)
    instance.save()
    return instance


@router.get("/periodic_task", response=List[SchemaOut])
@paginate(MyPagination)
def list_periodic_task(request):
    qs = retrieve(request, PeriodicTask)
    return qs


@router.get("/periodic_task/{periodic_task_id}", response=SchemaOut)
def get_periodic_task(request, periodic_task_id: int):
    qs = get_object_or_404(PeriodicTask, id=periodic_task_id)
    return qs


@router.get("/periodic_task/all/list", response=List[SchemaOut])
def all_list_role(request):
    qs = retrieve(request, PeriodicTask)
    return qs


class SchemaExecIn(Schema):
    task: str = None


@router.post("/periodic_task/immediate/exec")
def immediate_exec_task(request, data: SchemaExecIn):
    task_name = data.task
    data = {
        'task': None
    }
    test = f"""
from {'.'.join(task_name.split('.')[:-1])} import {task_name.split('.')[-1]}
task = {task_name.split('.')[-1]}.delay()
            """
    exec(test)

    return FuResponse()
