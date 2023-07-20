import json

from system.code_template.backend.mapping import component_to_search_type


def generator_backend_api(api_info):
    form_info = api_info.form_info
    form_info_dict = json.loads(form_info)
    filter_txt = ''
    field_code = ''

    for item in form_info_dict.get('schemas'):
        field_code = f''''{item['field']}', {field_code}'''
        column = f'''    
    {item['field']}: {component_to_search_type[item['component']]} = Field(None, alias='{item['field']}')'''
        filter_txt = column + filter_txt

    api_txt = f'''from typing import List
from .model import {api_info.code.capitalize()}
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
    {filter_txt}


# 设置请求接收字段
class {api_info.code.capitalize()}SchemaIn(ModelSchema):

    class Config:
        model = {api_info.code.capitalize()}
        model_exclude = ['create_datetime', 'update_datetime', 'belong_dept', 'modifier', 'creator', 'creator', 'id']


# 设置响应字段
class {api_info.code.capitalize()}SchemaOut(ModelSchema):

    class Config:
        model = {api_info.code.capitalize()}
        model_fields = '__all__'


# 创建{api_info.code.capitalize()}
@router.post('/{api_info.code}', response={api_info.code.capitalize()}SchemaOut)
def create_{api_info.code}(request, data: {api_info.code.capitalize()}SchemaIn):
    {api_info.code} = create(request, data, {api_info.code.capitalize()})
    return {api_info.code}


# 删除{api_info.code.capitalize()}
@router.delete('/{api_info.code}/{{id}}')
def delete_{api_info.code}(request, id: int):
    delete(id, {api_info.code.capitalize()})
    return {{'success': True}}


# 更新{api_info.code.capitalize()}
@router.put('/{api_info.code}/{{id}}', response={api_info.code.capitalize()}SchemaOut)
def update_{api_info.code}(request, id: int, data: {api_info.code.capitalize()}SchemaIn):
    {api_info.code} = update(request, id, data, {api_info.code.capitalize()})
    return {api_info.code}


# 获取{api_info.code.capitalize()}
@router.get('/{api_info.code}', response=List[{api_info.code.capitalize()}SchemaOut])
@paginate(MyPagination)
def list_{api_info.code}(request, filters: Filters = Query(...)):
    qs = retrieve(request, {api_info.code.capitalize()}, filters)
    return qs


# 导入
@router.get('/{api_info.code}/all/export')
def export_{api_info.code}(request):
    export_fields = ({field_code})
    return export_data(request, {api_info.code.capitalize()}, {api_info.code.capitalize()}SchemaOut, export_fields)


# 导出
@router.post('/{api_info.code}/all/import')
def import_{api_info.code}(request, data: ImportSchema):
    import_fields = ({field_code})
    return import_data(request, {api_info.code.capitalize()}, {api_info.code.capitalize()}SchemaIn, data, import_fields)
    '''
    return api_txt
