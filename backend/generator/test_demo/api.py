from typing import List
from .model import TestDemo
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
        
    des: str = Field(None, alias='des')    
    code: int = Field(None, alias='code')    
    name: str = Field(None, alias='name')


# 设置请求接收字段
class TestDemoSchemaIn(ModelSchema):

    class Config:
        model = TestDemo
        model_exclude = ['create_datetime', 'update_datetime', 'belong_dept', 'modifier', 'creator', 'creator', 'id']


# 设置响应字段
class TestDemoSchemaOut(ModelSchema):

    class Config:
        model = TestDemo
        model_fields = '__all__'


# 创建TestDemo
@router.post('/test_demo', response=TestDemoSchemaOut)
def create_test_demo(request, data: TestDemoSchemaIn):
    test_demo = create(request, data, TestDemo)
    return test_demo


# 删除TestDemo
@router.delete('/test_demo/{id}')
def delete_test_demo(request, id: int):
    delete(id, TestDemo)
    return {'success': True}


# 更新TestDemo
@router.put('/test_demo/{id}', response=TestDemoSchemaOut)
def update_test_demo(request, id: int, data: TestDemoSchemaIn):
    test_demo = update(request, id, data, TestDemo)
    return test_demo


# 获取TestDemo
@router.get('/test_demo', response=List[TestDemoSchemaOut])
@paginate(MyPagination)
def list_test_demo(request, filters: Filters = Query(...)):
    qs = retrieve(request, TestDemo, filters)
    return qs


# 导入
@router.get('/test_demo/all/export')
def export_test_demo(request):
    export_fields = ('des', 'code', 'name', )
    return export_data(request, TestDemo, TestDemoSchemaOut, export_fields)


# 导出
@router.post('/test_demo/all/import')
def import_test_demo(request, data: ImportSchema):
    import_fields = ('des', 'code', 'name', )
    return import_data(request, TestDemo, TestDemoSchemaIn, data, import_fields)
    