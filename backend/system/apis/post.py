# -*- coding: utf-8 -*-
# @Time    : 2022/5/10 21:56
# @Author  : 臧成龙
# @FileName: post.py
# @Software: PyCharm

from typing import List

from django.shortcuts import get_object_or_404
from ninja import Field, ModelSchema, Query, Router, Schema, UploadedFile
from ninja.pagination import paginate
from system.models import Post
from utils.fu_crud import (
    ImportSchema,
    create,
    delete,
    export_data,
    import_data,
    retrieve,
    update,
)
from utils.fu_ninja import FuFilters, MyPagination

router = Router()


class Filters(FuFilters):
    name: str = Field(None, alias="name")
    code: str = Field(None, alias="code")
    status: int = Field(None, alias="status")

    id: str = Field(None, alias="post_id")


class PostSchemaIn(ModelSchema):
    class Config:
        model = Post
        model_fields = ['name', 'code', 'sort', 'status']


class PostSchemaOut(ModelSchema):
    class Config:
        model = Post
        model_fields = "__all__"


@router.post("/post", response=PostSchemaOut)
def create_post(request, data: PostSchemaIn):
    post = create(request, data, Post)
    return post


@router.delete("/post/{post_id}")
def delete_post(request, post_id: int):
    delete(post_id, Post)
    return {"success": True}


@router.put("/post/{post_id}", response=PostSchemaOut)
def update_post(request, post_id: int, data: PostSchemaIn):
    post = update(request, post_id, data, Post)
    return post


@router.get("/post", response=List[PostSchemaOut])
@paginate(MyPagination)
def list_post(request, filters: Filters = Query(...)):
    qs = retrieve(request, Post, filters)
    return qs


@router.get("/post/{post_id}", response=PostSchemaOut)
def get_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    return post


@router.get("/post/all/list", response=List[PostSchemaOut])
def all_list_post(request):
    qs = retrieve(request, Post)
    return qs


@router.get("/post/all/export")
def export_post(request):
    export_fields = ['name', 'code', 'status', 'sort']
    return export_data(request, Post, PostSchemaOut, export_fields)


@router.post("/post/all/import")
def import_post(request, data: ImportSchema):
    import_fields = ['name', 'code', 'status', 'sort']
    return import_data(request, Post, PostSchemaIn, data, import_fields)

