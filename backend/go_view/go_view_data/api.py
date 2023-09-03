from typing import List
from .model import GoViewData
from ninja import Field, ModelSchema, Query, Router
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
        
    content: str = Field(None, alias='content')    
    project_id: str = Field(None, alias='project_id')


# 设置请求接收字段
class GoViewDataSchemaIn(ModelSchema):

    class Config:
        model = GoViewData
        model_exclude = ['create_datetime', 'update_datetime', 'belong_dept', 'modifier', 'creator', 'creator', 'id']


# 设置响应字段
class GoViewDataSchemaOut(ModelSchema):

    class Config:
        model = GoViewData
        model_fields = '__all__'


# 创建GoViewData
@router.post('/go_view_data', response=GoViewDataSchemaOut)
def create_go_view_data(request, data: GoViewDataSchemaIn):
    go_view_data = create(request, data, GoViewData)
    return go_view_data


# 删除GoViewData
@router.delete('/go_view_data/{id}')
def delete_go_view_data(request, id: int):
    delete(id, GoViewData)
    return {'success': True}


# 更新GoViewData
@router.put('/go_view_data/{id}', response=GoViewDataSchemaOut)
def update_go_view_data(request, id: int, data: GoViewDataSchemaIn):
    go_view_data = update(request, id, data, GoViewData)
    return go_view_data


# 获取GoViewData
@router.get('/go_view_data', response=List[GoViewDataSchemaOut])
@paginate(MyPagination)
def list_go_view_data(request, filters: Filters = Query(...)):
    qs = retrieve(request, GoViewData, filters)
    return qs


# 导入
@router.get('/go_view_data/all/export')
def export_go_view_data(request):
    export_fields = ('content', 'project_id', )
    return export_data(request, GoViewData, GoViewDataSchemaOut, export_fields)


# 导出
@router.post('/go_view_data/all/import')
def import_go_view_data(request, data: ImportSchema):
    import_fields = ('content', 'project_id', )
    return import_data(request, GoViewData, GoViewDataSchemaIn, data, import_fields)
    