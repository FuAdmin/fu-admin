from typing import List
from .model import TestOne
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
        
    input_number_3: int = Field(None, alias='input_number_3')    
    input_text_area_2: str = Field(None, alias='input_text_area_2')    
    input_1: str = Field(None, alias='input_1')


# 设置请求接收字段
class TestOneSchemaIn(ModelSchema):

    class Config:
        model = TestOne
        model_exclude = ['create_datetime', 'update_datetime', 'belong_dept', 'modifier', 'creator', 'creator', 'id']


# 设置响应字段
class TestOneSchemaOut(ModelSchema):

    class Config:
        model = TestOne
        model_fields = '__all__'


# 创建TestOne
@router.post('/test_one', response=TestOneSchemaOut)
def create_test_one(request, data: TestOneSchemaIn):
    test_one = create(request, data, TestOne)
    return test_one


# 删除TestOne
@router.delete('/test_one/{id}')
def delete_test_one(request, id: int):
    delete(id, TestOne)
    return {'success': True}


# 更新TestOne
@router.put('/test_one/{id}', response=TestOneSchemaOut)
def update_test_one(request, id: int, data: TestOneSchemaIn):
    test_one = update(request, id, data, TestOne)
    return test_one


# 获取TestOne
@router.get('/test_one', response=List[TestOneSchemaOut])
@paginate(MyPagination)
def list_test_one(request, filters: Filters = Query(...)):
    qs = retrieve(request, TestOne, filters)
    return qs


# 导入
@router.get('/test_one/all/export')
def export_test_one(request):
    export_fields = ('input_number_3', 'input_text_area_2', 'input_1', )
    return export_data(request, TestOne, TestOneSchemaOut, export_fields)


# 导出
@router.post('/test_one/all/import')
def import_test_one(request, data: ImportSchema):
    import_fields = ('input_number_3', 'input_text_area_2', 'input_1', )
    return import_data(request, TestOne, TestOneSchemaIn, data, import_fields)
    