# from application.ninja_cof import api
# Author 臧成龙
# coding=utf-8
# @Time    : 2022/5/21 02:36
# @File    : button.py
# @Software: PyCharm
# @qq: 939589097

from typing import List

from django.shortcuts import get_object_or_404
from ninja import Field, ModelSchema, Query, Router, Schema
from ninja.pagination import paginate
from system.models import Button
from utils.fu_ninja import MyPagination

router = Router()


class Filters(Schema):
    name: str = Field(None, alias="name")
    code: str = Field(None, alias="code")
    id: str = Field(None, alias="id")


class SchemaIn(ModelSchema):

    class Config:
        model = Button
        model_exclude = ['id', 'create_datetime', 'update_datetime']


class SchemaOut(ModelSchema):
    class Config:
        model = Button
        model_fields = "__all__"
    # model_fields = []


@router.post("/button", response=SchemaOut)
def create_button(request, data: SchemaIn):
    post = Button.objects.create(**data.dict())
    return post


@router.get("/button/{button_id}", response=SchemaOut)
def get_button(request, button_id: int):
    post = get_object_or_404(Button, id=button_id)
    return post


@router.get("/button", response=List[SchemaOut])
@paginate(MyPagination)
def list_button(request, filters: Filters = Query(...)):
    qs = Button.objects.filter(**filters.dict(exclude_none=True))
    return qs


@router.get("/button/all/list", response=List[SchemaOut])
def all_list_button(request):
    qs = Button.objects.all()
    return qs


@router.put("/button/{button_id}", response=SchemaOut)
def update_button(request, button_id: int, payload: SchemaIn):
    post = get_object_or_404(Button, id=button_id)
    for attr, value in payload.dict().items():
        setattr(post, attr, value)
    post.save()
    return post


@router.delete("/button/{button_id}")
def delete_button(request, button_id: int):
    post = get_object_or_404(Button, id=button_id)
    post.delete()
    return {"success": True}

