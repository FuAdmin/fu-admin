# -*- coding: utf-8 -*-
# @Time    : 2022/5/10 21:56
# @Author  : 臧成龙
# @FileName: generator_template.py
# @Software: PyCharm
import os
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Field, ModelSchema, Query, Router, Schema, UploadedFile
from ninja.pagination import paginate

from system.apis.code_generator.code_template.web.api_template import generator_api
from system.apis.code_generator.code_template.web.data_template import generator_data
from system.apis.code_generator.code_template.web.drawer_template import generator_drawer
from system.apis.code_generator.code_template.web.index_template import generator_index
from system.models import GeneratorTemplate, Menu, MenuButton
from utils.fu_crud import (
    ImportSchema,
    create,
    delete,
    export_data,
    import_data,
    retrieve,
    update, batch_create,
)
from utils.fu_ninja import FuFilters, MyPagination

router = Router()


class Filters(FuFilters):
    name: str = Field(None, alias="name")
    code: str = Field(None, alias="code")
    id: str = Field(None, alias="id")


class GeneratorTemplateSchemaIn(ModelSchema):
    class Config:
        model = GeneratorTemplate
        model_fields = ['name', 'code', 'form_info', 'table_info', 'remark']


class GeneratorTemplateSchemaOut(ModelSchema):
    class Config:
        model = GeneratorTemplate
        model_fields = "__all__"


@router.post("/generator_template", response=GeneratorTemplateSchemaOut)
def create_generator_template(request, data: GeneratorTemplateSchemaIn):
    generator_template = create(request, data, GeneratorTemplate)
    return generator_template


@router.delete("/generator_template/{generator_template_id}")
def delete_generator_template(request, generator_template_id: int):
    delete(generator_template_id, GeneratorTemplate)
    return {"success": True}


@router.put("/generator_template/{generator_template_id}", response=GeneratorTemplateSchemaOut)
def update_generator_template(request, generator_template_id: int, data: GeneratorTemplateSchemaIn):
    generator_template = update(request, generator_template_id, data, GeneratorTemplate)
    return generator_template


@router.get("/generator_template", response=List[GeneratorTemplateSchemaOut])
@paginate(MyPagination)
def list_generator_template(request, filters: Filters = Query(...)):
    qs = retrieve(request, GeneratorTemplate, filters)
    return qs


@router.get("/generator_template/{generator_template_id}", response=GeneratorTemplateSchemaOut)
def get_generator_template(request, generator_template_id: int):
    generator_template = get_object_or_404(GeneratorTemplate, id=generator_template_id)
    return generator_template


@router.get("/generator_template/all/list", response=List[GeneratorTemplateSchemaOut])
def all_list_generator_template(request):
    qs = retrieve(request, GeneratorTemplate)
    return qs


@router.get("/generator_template/all/export")
def export_generator_template(request):
    export_fields = ['name', 'code', 'status', 'sort']
    return export_data(request, GeneratorTemplate, GeneratorTemplateSchemaOut, export_fields)


@router.post("/generator_template/all/import")
def import_generator_template(request, data: ImportSchema):
    import_fields = ['name', 'code', 'status', 'sort']
    return import_data(request, GeneratorTemplate, GeneratorTemplateSchemaIn, data, import_fields)


@router.put("/generator_template/code/generate/{generator_template_id}", response=GeneratorTemplateSchemaOut)
def update_generator_template(request, generator_template_id: int):
    instance = get_object_or_404(GeneratorTemplate, id=generator_template_id)
    web_index_txt = generator_index(instance)
    web_data_txt = generator_data(instance)
    web_drawer_txt = generator_drawer(instance)
    web_api_txt = generator_api(instance)
    web_target_path = os.path.abspath(
        os.path.join(os.getcwd(), "..", 'web', 'src', 'views', 'generator-project', instance.code))
    # 判断当前路径是否存在，没有则创建文件夹
    if not os.path.exists(web_target_path):
        os.makedirs(web_target_path)

    web_index_path = os.path.join(web_target_path, 'index.vue')
    with open(web_index_path, 'w', encoding='utf-8') as file:
        file.write(web_index_txt)

    web_data_path = os.path.join(web_target_path, 'data.ts')
    with open(web_data_path, 'w', encoding='utf-8') as file:
        file.write(web_data_txt)

    web_api_path = os.path.join(web_target_path, 'api.ts')
    with open(web_api_path, 'w', encoding='utf-8') as file:
        file.write(web_api_txt)

    web_drawer_path = os.path.join(web_target_path, 'drawer.vue')
    with open(web_drawer_path, 'w', encoding='utf-8') as file:
        file.write(web_drawer_txt)
    # 添加菜单和菜单按钮
    if not instance.has_menu:
        # 添加菜单
        menu_dic = {
            "type": 1,
            "title": instance.name,
            "parent_id": 33,
            "sort": 1,
            "icon": "ant-design:book-outlined",
            "path": instance.code,
            "status": True,
            "hide_menu": False,
            "component": f"/generator-project/{instance.code}/index.vue",
            "name": instance.code,
            "is_ext": False,
            "keepalive": False
        }
        menu_qr = create(request, menu_dic, Menu)
        # 添加菜单按钮
        button_list = [
            {
                "name": "新增",
                "code": f"{instance.code}:add",
                "method": 1,
                "api": f"/api/generator_project/{instance.code}",
                "sort": 1,
                "menu_id": menu_qr.id
            },
            {
                "name": "删除",
                "code": f"{instance.code}:delete",
                "method": 2,
                "api": f"/api/generator_project/{instance.code}/{instance.code}_id",
                "sort": 2,
                "menu_id": menu_qr.id
            },
            {
                "name": "修改",
                "code": f"{instance.code}:update",
                "method": 3,
                "api": f"/api/generator_project/{instance.code}/{instance.code}_id",
                "sort": 3,
                "menu_id": menu_qr.id
            },
            {
                "name": "查询",
                "code": f"{instance.code}:search",
                "method": 0,
                "api": f"/api/generator_project/{instance.code}",
                "sort": 4,
                "menu_id": menu_qr.id
            }
        ]
        batch_create(request, button_list, MenuButton)
        instance.has_menu = True
        instance.save()

    return 'generator_template'
