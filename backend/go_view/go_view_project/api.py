from typing import List

from django.db import connection
from django.shortcuts import get_object_or_404

from utils.usual import query_all_dict, get_user_info_from_token
from .model import GoViewProject
from ninja import Field, ModelSchema, Query, Router, Schema
from ninja.pagination import paginate
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
from ..go_view_data.model import GoViewData

router = Router()


# 设置过滤字段
class Filters(FuFilters):
    index_image: str = Field(None, alias='indexImage')
    state: int = Field(None, alias='state')
    project_name: str = Field(None, alias='projectName')
    id: int = Field(default=None, alias='projectId')


# 设置请求接收字段
class GoViewProjectSchemaIn(Schema):
    index_image: str = Field(None, alias='indexImage')
    state: int = Field(-1, alias='state')
    project_name: str = Field(None, alias='projectName')
    content: str = Field(None, alias='content')


class GoViewProjectSqlIn(Schema):
    sql: str = Field(None, alias='sql')


class GoViewProjectSchemaUpdate(Schema):
    content: str = Field(None, alias='content')
    id: int = Field(default=None, alias='projectId')


# 设置响应字段
class GoViewProjectSchemaOut(ModelSchema):
    indexImage: str = Field(None, alias='index_image')
    projectName: str = Field(None, alias='project_name')

    # content: str = Field(None, alias='content')

    class Config:
        model = GoViewProject
        model_fields = '__all__'


# 创建GoViewProject
@router.post('/project', response=GoViewProjectSchemaOut, auth=None)
def create_project(request, data: GoViewProjectSchemaIn):
    project = create(request, data, GoViewProject)
    return project


@router.post('/project/request/sql', response=List)
def create_project(request, data: GoViewProjectSqlIn):
    # 真正的原生sql,
    query_list = query_all_dict(data.sql)
    return query_list


@router.post('/project/save/data', response=GoViewProjectSchemaOut)
def create_project(request, data: GoViewProjectSchemaUpdate):
    project = update(request, data.id, data, GoViewProject)
    return project


# 删除GoViewProject
@router.delete('/project/{id}')
def delete_project(request, id: int):
    delete(id, GoViewProject)
    return {'success': True}


# 更新GoViewProject
@router.put('/project/{id}', response=GoViewProjectSchemaOut)
def update_project(request, id: int, data: GoViewProjectSchemaIn):
    project = update(request, id, data, GoViewProject)
    return project


# 发布
@router.put('/project/publish/by_id/{id}', response=GoViewProjectSchemaOut)
def publish_project(request, id: int, data: GoViewProjectSchemaIn):
    instance = get_object_or_404(GoViewProject, id=id)
    user_info = get_user_info_from_token(request)
    # 修改时默认添加修改者
    instance.state = data.state
    instance.modifier = user_info['name']
    instance.save()
    return instance


# 获取GoViewProject
@router.get('/project', response=List[GoViewProjectSchemaOut])
@paginate(MyPagination)
def list_project(request, filters: Filters = Query(...)):
    qs = retrieve(request, GoViewProject, filters)
    return qs


@router.get('/project/by/id', response=GoViewProjectSchemaOut)
def list_project(request, filters: Filters = Query(...)):
    qs = GoViewProject.objects.get(id=filters.id)
    return qs


# 导入
@router.get('/project/all/export')
def export_project(request):
    export_fields = ('index_image', 'state', 'project_name',)
    return export_data(request, GoViewProject, GoViewProjectSchemaOut, export_fields)


# 导出
@router.post('/project/all/import')
def import_project(request, data: ImportSchema):
    import_fields = ('index_image', 'state', 'project_name',)
    return import_data(request, GoViewProject, GoViewProjectSchemaIn, data, import_fields)
