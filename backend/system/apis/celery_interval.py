# -*- coding: utf-8 -*-
# @Time    : 2022/6/14 00:32
# @Author  : 臧成龙
# @FileName: interval_schedule.py
# @Software: PyCharm
from typing import List

from django.shortcuts import get_object_or_404
from django_celery_beat.models import IntervalSchedule
from ninja import ModelSchema, Router
from ninja.pagination import paginate
from utils.fu_crud import create, delete, retrieve, update
from utils.fu_ninja import MyPagination

router = Router()


class SchemaIn(ModelSchema):
    class Config:
        model = IntervalSchedule
        model_fields = ['every', 'period']


class SchemaOut(ModelSchema):
    class Config:
        model = IntervalSchedule
        model_fields = ['id', 'every', 'period']


@router.post("/interval_schedule", response=SchemaOut)
def create_interval_schedule(request, data: SchemaIn):
    qs = IntervalSchedule.objects.create(**data.dict())
    return qs


@router.delete("/interval_schedule/{interval_schedule_id}")
def delete_interval_schedule(request, interval_schedule_id: int):
    delete(interval_schedule_id, IntervalSchedule)
    return {"success": True}


@router.put("/interval_schedule/{interval_schedule_id}", response=SchemaOut)
def update_interval_schedule(request, interval_schedule_id: int, data: SchemaIn):
    instance = get_object_or_404(IntervalSchedule, id=interval_schedule_id)
    for attr, value in data.dict().items():
        setattr(instance, attr, value)
    instance.save()
    return instance


@router.get("/interval_schedule", response=List[SchemaOut])
@paginate(MyPagination)
def list_interval_schedule(request):
    qs = retrieve(request, IntervalSchedule)
    return qs


@router.get("/interval_schedule/{interval_schedule_id}", response=SchemaOut)
def get_interval_schedule(request, interval_schedule_id: int):
    qs = get_object_or_404(IntervalSchedule, id=interval_schedule_id)
    return qs


@router.get("/interval_schedule/all/list", response=List[SchemaOut])
def all_list_role(request):
    qs = retrieve(request, IntervalSchedule)
    return qs
