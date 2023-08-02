from typing import List
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

router = Router()


# 设置过滤字段
class Filters(FuFilters):
    index_image: str = Field(None, alias='indexImage')
    state: str = Field(None, alias='state')
    project_name: str = Field(None, alias='projectName')


# 设置请求接收字段
class GoViewProjectSchemaIn(Schema):
    index_image: str = Field(None, alias='indexImage')
    state: str = Field(None, alias='state')
    project_name: str = Field(None, alias='projectName')


# 设置响应字段
class GoViewProjectSchemaOut(ModelSchema):
    indexImage: str = Field(None, alias='index_image')
    projectName: str = Field(None, alias='project_name')

    class Config:
        model = GoViewProject
        model_fields = '__all__'


# 创建GoViewProject
@router.post('/project', response=GoViewProjectSchemaOut, auth=None)
def create_project(request, data: GoViewProjectSchemaIn):
    project = create(request, data, GoViewProject)
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


# 获取GoViewProject
@router.get('/project', response=List[GoViewProjectSchemaOut])
@paginate(MyPagination)
def list_project(request, filters: Filters = Query(...)):
    qs = retrieve(request, GoViewProject, filters)
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
