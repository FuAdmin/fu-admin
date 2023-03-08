# -*- coding: utf-8 -*-
# @Time    : 2022/6/14 00:13
# @Author  : 臧成龙
# @FileName: crontab_schedule.py
# @Software: PyCharm
from typing import List

from django.shortcuts import get_object_or_404
from django_celery_beat.models import CrontabSchedule
from ninja import ModelSchema, Router
from ninja.pagination import paginate
from utils.fu_crud import create, delete, retrieve, update
from utils.fu_ninja import MyPagination

router = Router()


class SchemaIn(ModelSchema):
    class Config:
        model = CrontabSchedule
        model_fields = ['minute', 'hour', 'day_of_month', 'month_of_year', 'day_of_week']


class SchemaOut(ModelSchema):
    class Config:
        model = CrontabSchedule
        model_fields = ['id', 'minute', 'hour', 'day_of_month', 'month_of_year', 'day_of_week']


@router.post("/crontab_schedule", response=SchemaOut)
def create_crontab_schedule(request, data: SchemaIn):
    qs = CrontabSchedule.objects.create(**data.dict())
    return qs


@router.delete("/crontab_schedule/{crontab_schedule_id}")
def delete_crontab_schedule(request, crontab_schedule_id: int):
    delete(crontab_schedule_id, CrontabSchedule)
    return {"success": True}


@router.put("/crontab_schedule/{crontab_schedule_id}", response=SchemaOut)
def update_crontab_schedule(request, crontab_schedule_id: int, data: SchemaIn):
    instance = get_object_or_404(CrontabSchedule, id=crontab_schedule_id)
    for attr, value in data.dict().items():
        setattr(instance, attr, value)
    instance.save()
    return instance


@router.get("/crontab_schedule", response=List[SchemaOut])
@paginate(MyPagination)
def list_crontab_schedule(request):
    qs = retrieve(request, CrontabSchedule)
    return qs


@router.get("/crontab_schedule/{crontab_schedule_id}", response=SchemaOut)
def get_crontab_schedule(request, crontab_schedule_id: int):
    qs = get_object_or_404(CrontabSchedule, id=crontab_schedule_id)
    return qs


@router.get("/crontab_schedule/all/list", response=List[SchemaOut])
def all_list_role(request):
    qs = retrieve(request, CrontabSchedule)
    return qs
