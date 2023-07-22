from typing import List
from .model import Test
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
        
    icon: str = Field(None, alias='icon')    
    sequence: int = Field(None, alias='sequence')    
    code: str = Field(None, alias='code')    
    name: str = Field(None, alias='name')


# 设置请求接收字段
class TestSchemaIn(ModelSchema):

    class Config:
        model = Test
        model_exclude = ['create_datetime', 'update_datetime', 'belong_dept', 'modifier', 'creator', 'creator', 'id']


# 设置响应字段
class TestSchemaOut(ModelSchema):

    class Config:
        model = Test
        model_fields = '__all__'


# 创建Test
@router.post('/test', response=TestSchemaOut)
def create_test(request, data: TestSchemaIn):
    test = create(request, data, Test)
    return test


# 删除Test
@router.delete('/test/{id}')
def delete_test(request, id: int):
    delete(id, Test)
    return {'success': True}


# 更新Test
@router.put('/test/{id}', response=TestSchemaOut)
def update_test(request, id: int, data: TestSchemaIn):
    test = update(request, id, data, Test)
    return test


# 获取Test
@router.get('/test', response=List[TestSchemaOut])
@paginate(MyPagination)
def list_test(request, filters: Filters = Query(...)):
    qs = retrieve(request, Test, filters)
    return qs


# 导入
@router.get('/test/all/export')
def export_test(request):
    export_fields = ('icon', 'sequence', 'code', 'name', )
    return export_data(request, Test, TestSchemaOut, export_fields)


# 导出
@router.post('/test/all/import')
def import_test(request, data: ImportSchema):
    import_fields = ('icon', 'sequence', 'code', 'name', )
    return import_data(request, Test, TestSchemaIn, data, import_fields)
    