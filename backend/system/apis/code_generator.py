# -*- coding: utf-8 -*-
# @Time    : 2022/5/10 21:56
# @Author  : 臧成龙
# @FileName: generator_template.py
# @Software: PyCharm
import json
import os
import subprocess
from typing import List

from django.core import management
from django.shortcuts import get_object_or_404
from ninja import Field, ModelSchema, Query, Router
from ninja.pagination import paginate

from system.code_template.backend.api import generator_backend_api
from system.code_template.backend.model import generator_backend_model
from system.code_template.backend.router import generator_router
from system.code_template.web.api_template import generator_api
from system.code_template.web.data_template import generator_data
from system.code_template.web.drawer_template import generator_drawer
from system.code_template.web.index_template import generator_index
from system.models import GeneratorTemplate, Menu, MenuButton, MenuColumnField
from utils.fu_crud import (
    ImportSchema,
    create,
    delete,
    export_data,
    import_data,
    retrieve,
    update, batch_create, )
from utils.fu_ninja import FuFilters, MyPagination
from utils.fu_response import FuResponse
from utils.usual import insert_content_after_line

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


@router.put("/generator_template/code/generate/{generator_template_id}")
def generate_code(request, generator_template_id: int):
    instance = get_object_or_404(GeneratorTemplate, id=generator_template_id)
    web_index_txt = generator_index(instance)
    web_data_txt = generator_data(instance)
    web_drawer_txt = generator_drawer(instance)
    web_api_txt = generator_api(instance)
    web_target_path = os.path.abspath(
        os.path.join(os.getcwd(), "..", 'web', 'src', 'views', 'generator', instance.code))
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
    # 添加列表字段，菜单和菜单按钮
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
            "component": f"/generator/{instance.code}/index.vue",
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
                "api": f"/api/generator/{instance.code}",
                "sort": 1,
                "menu_id": menu_qr.id
            },
            {
                "name": "删除",
                "code": f"{instance.code}:delete",
                "method": 3,
                "api": f"/api/generator/{instance.code}/{instance.code}_id",
                "sort": 2,
                "menu_id": menu_qr.id
            },
            {
                "name": "修改",
                "code": f"{instance.code}:update",
                "method": 2,
                "api": f"/api/generator/{instance.code}/{instance.code}_id",
                "sort": 3,
                "menu_id": menu_qr.id
            },
            {
                "name": "查询",
                "code": f"{instance.code}:search",
                "method": 0,
                "api": f"/api/generator/{instance.code}",
                "sort": 4,
                "menu_id": menu_qr.id
            }
        ]
        batch_create(request, button_list, MenuButton)

        # 添加列表字段
        table_info = json.loads(instance.table_info)
        column_info = table_info.get('columnInfo')
        column_list = []
        for item in column_info:
            column_list.append({
                'code': instance.code + ':' + item['field_name'],
                'name': item['column_name'],
                'menu_id': menu_qr.id,
            })
        batch_create(request, column_list, MenuColumnField)

    # 生成后端代码
    backend_model_txt = generator_backend_model(instance)
    backend_api_txt = generator_backend_api(instance)
    backend_router_txt = generator_router(instance)

    # 更新generator router
    generator_router_path = os.path.abspath(os.path.join(os.getcwd(), 'generator', 'router.py'))

    if not instance.has_menu:
        insert_from_txt = f'''from .{instance.code}.api import router as {instance.code}_router'''
        insert_content_after_line(generator_router_path, 'from ninja import Router', insert_from_txt)
        insert_router_txt = f'''generator_router.add_router('/', {instance.code}_router, tags=['{instance.name}'])'''
        insert_content_after_line(generator_router_path, 'generator_router = Router()', insert_router_txt)
    instance.has_menu = True
    instance.save()

    backend_target_path = os.path.abspath(os.path.join(os.getcwd(), 'generator', instance.code))

    # 判断当前路径是否存在，没有则创建文件夹
    if not os.path.exists(backend_target_path):
        os.makedirs(backend_target_path)
    backend_model_path = os.path.join(backend_target_path, 'model.py')
    with open(backend_model_path, 'w', encoding='utf-8') as file:
        file.write(backend_model_txt)

    backend_api_path = os.path.join(backend_target_path, 'api.py')
    with open(backend_api_path, 'w', encoding='utf-8') as file:
        file.write(backend_api_txt)

    backend_router_path = os.path.join(backend_target_path, 'router.py')
    with open(backend_router_path, 'w', encoding='utf-8') as file:
        file.write(backend_router_txt)

    return FuResponse(msg='代码生成成功')


@router.put("/generator_template/code/generate_db/{generator_template_id}")
def generate_db(request, generator_template_id: int):
    management.call_command('makemigrations','generator')
    management.call_command('migrate','generator')
    return FuResponse(msg='数据库生成成功')
