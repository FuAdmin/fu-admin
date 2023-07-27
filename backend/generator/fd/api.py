from typing import List
from .model import Fd
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
        
    select_1: str = Field(None, alias='select_1')    
    input_number_2: int = Field(None, alias='input_number_2')    
    input_1: str = Field(None, alias='input_1')


# 设置请求接收字段
class FdSchemaIn(ModelSchema):

    class Config:
        model = Fd
        model_exclude = ['create_datetime', 'update_datetime', 'belong_dept', 'modifier', 'creator', 'creator', 'id']


# 设置响应字段
class FdSchemaOut(ModelSchema):

    class Config:
        model = Fd
        model_fields = '__all__'


# 创建Fd
@router.post('/fd', response=FdSchemaOut)
def create_fd(request, data: FdSchemaIn):
    fd = create(request, data, Fd)
    return fd


# 删除Fd
@router.delete('/fd/{id}')
def delete_fd(request, id: int):
    delete(id, Fd)
    return {'success': True}


# 更新Fd
@router.put('/fd/{id}', response=FdSchemaOut)
def update_fd(request, id: int, data: FdSchemaIn):
    fd = update(request, id, data, Fd)
    return fd


# 获取Fd
@router.get('/fd', response=List[FdSchemaOut])
@paginate(MyPagination)
def list_fd(request, filters: Filters = Query(...)):
    qs = retrieve(request, Fd, filters)
    return qs


# 导入
@router.get('/fd/all/export')
def export_fd(request):
    export_fields = ('select_1', 'input_number_2', 'input_1', )
    return export_data(request, Fd, FdSchemaOut, export_fields)


# 导出
@router.post('/fd/all/import')
def import_fd(request, data: ImportSchema):
    import_fields = ('select_1', 'input_number_2', 'input_1', )
    return import_data(request, Fd, FdSchemaIn, data, import_fields)
    