# -*- coding: utf-8 -*-
# @Time    : 2022/6/07 00:56
# @Author  : 臧成龙
# @FileName: file.py
# @Software: PyCharm
import os
from datetime import datetime
from typing import List
from urllib.parse import unquote

from django.http import FileResponse, StreamingHttpResponse, HttpResponse
from django.shortcuts import get_object_or_404
from fuadmin.settings import BASE_DIR, STATIC_URL
from ninja import Field
from ninja import File as NinjaFile
from ninja import ModelSchema, Query, Router, Schema
from ninja.files import UploadedFile
from ninja.pagination import paginate
from system.models import File
from utils.fu_crud import create, delete, retrieve, update
from utils.fu_ninja import FuFilters, MyPagination

router = Router()


class Filters(FuFilters):
    name: str = Field(None, alias="name")


class SchemaIn(Schema):
    name: str = Field(None, alias="name")
    url: str = Field(None, alias="url")


class SchemaOut(ModelSchema):
    class Config:
        model = File
        model_fields = "__all__"


@router.delete("/file/{file_id}")
def delete_file(request, file_id: int):
    delete(file_id, File)
    return {"success": True}


@router.get("/file", response=List[SchemaOut])
@paginate(MyPagination)
def list_file(request, filters: Filters = Query(...)):
    qs = retrieve(request, File, filters)
    return qs


@router.get("/file/{file_id}", response=SchemaOut)
def get_file(request, file_id: int):
    qs = get_object_or_404(File, id=file_id)
    return qs


@router.get("/file/all/list", response=List[SchemaOut])
def all_list_role(request):
    qs = retrieve(request, File)
    return qs


@router.post("/upload", response=SchemaOut)
def upload(request, file: UploadedFile = NinjaFile(...)):
    binary_data = file.read()
    current_date = datetime.now().strftime('%Y%m%d%H%M%S%f')
    current_ymd = datetime.now().strftime('%Y%m%d')
    file_name = current_date + '_' + file.name.replace(' ', '_')
    file_path = os.path.join(STATIC_URL, current_ymd)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file_url = os.path.join(file_path, file_name)
    with open(file_url, 'wb') as f:
        f.write(binary_data)
    data = {
        'name': file.name,
        'size': file.size,
        'save_name': file_name,
        'url': file_url,
    }
    qs = create(request, data, File)
    return qs


@router.post("/download")
def create_post(request, data: SchemaIn):
    filePath = str(BASE_DIR) + unquote(data.url)
    r = FileResponse(open(filePath, "rb"), as_attachment=True)
    return r


@router.get("/image/{image_id}", auth=None)
def get_file(request, image_id: int):
    qs = get_object_or_404(File, id=image_id)

    return HttpResponse(open(os.path.join(str(BASE_DIR), str(qs.url)), "rb"), content_type='image/png')
