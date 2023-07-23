from typing import List
from .model import TemplateTest
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
        
    input_text_area_2: str = Field(None, alias='input_text_area_2')    
    input_1: str = Field(None, alias='input_1')


# 设置请求接收字段
class TemplateTestSchemaIn(ModelSchema):

    class Config:
        model = TemplateTest
        model_exclude = ['create_datetime', 'update_datetime', 'belong_dept', 'modifier', 'creator', 'creator', 'id']


# 设置响应字段
class TemplateTestSchemaOut(ModelSchema):

    class Config:
        model = TemplateTest
        model_fields = '__all__'


# 创建TemplateTest
@router.post('/template_test', response=TemplateTestSchemaOut)
def create_template_test(request, data: TemplateTestSchemaIn):
    template_test = create(request, data, TemplateTest)
    return template_test


# 删除TemplateTest
@router.delete('/template_test/{id}')
def delete_template_test(request, id: int):
    delete(id, TemplateTest)
    return {'success': True}


# 更新TemplateTest
@router.put('/template_test/{id}', response=TemplateTestSchemaOut)
def update_template_test(request, id: int, data: TemplateTestSchemaIn):
    template_test = update(request, id, data, TemplateTest)
    return template_test


# 获取TemplateTest
@router.get('/template_test', response=List[TemplateTestSchemaOut])
@paginate(MyPagination)
def list_template_test(request, filters: Filters = Query(...)):
    qs = retrieve(request, TemplateTest, filters)
    return qs


# 导入
@router.get('/template_test/all/export')
def export_template_test(request):
    export_fields = ('input_text_area_2', 'input_1', )
    return export_data(request, TemplateTest, TemplateTestSchemaOut, export_fields)


# 导出
@router.post('/template_test/all/import')
def import_template_test(request, data: ImportSchema):
    import_fields = ('input_text_area_2', 'input_1', )
    return import_data(request, TemplateTest, TemplateTestSchemaIn, data, import_fields)
    