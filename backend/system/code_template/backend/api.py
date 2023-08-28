import json

from system.code_template.backend.mapping import component_to_search_type
from utils.ru_convert import RuleConvert


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
from .model import {RuleConvert.to_upper_camel_case(api_info.code)}
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
class {RuleConvert.to_upper_camel_case(api_info.code)}SchemaIn(ModelSchema):

    class Config:
        model = {RuleConvert.to_upper_camel_case(api_info.code)}
        model_exclude = ['create_datetime', 'update_datetime', 'belong_dept', 'modifier', 'creator', 'id']


# 设置响应字段
class {RuleConvert.to_upper_camel_case(api_info.code)}SchemaOut(ModelSchema):

    class Config:
        model = {RuleConvert.to_upper_camel_case(api_info.code)}
        model_fields = '__all__'


# 创建{RuleConvert.to_upper_camel_case(api_info.code)}
@router.post('/{api_info.code}', response={RuleConvert.to_upper_camel_case(api_info.code)}SchemaOut)
def create_{api_info.code}(request, data: {RuleConvert.to_upper_camel_case(api_info.code)}SchemaIn):
    {api_info.code} = create(request, data, {RuleConvert.to_upper_camel_case(api_info.code)})
    return {api_info.code}


# 删除{RuleConvert.to_upper_camel_case(api_info.code)}
@router.delete('/{api_info.code}/{{id}}')
def delete_{api_info.code}(request, id: int):
    delete(id, {RuleConvert.to_upper_camel_case(api_info.code)})
    return {{'success': True}}


# 更新{RuleConvert.to_upper_camel_case(api_info.code)}
@router.put('/{api_info.code}/{{id}}', response={RuleConvert.to_upper_camel_case(api_info.code)}SchemaOut)
def update_{api_info.code}(request, id: int, data: {RuleConvert.to_upper_camel_case(api_info.code)}SchemaIn):
    {api_info.code} = update(request, id, data, {RuleConvert.to_upper_camel_case(api_info.code)})
    return {api_info.code}


# 获取{RuleConvert.to_upper_camel_case(api_info.code)}
@router.get('/{api_info.code}', response=List[{RuleConvert.to_upper_camel_case(api_info.code)}SchemaOut])
@paginate(MyPagination)
def list_{api_info.code}(request, filters: Filters = Query(...)):
    qs = retrieve(request, {RuleConvert.to_upper_camel_case(api_info.code)}, filters)
    return qs


# 导入
@router.get('/{api_info.code}/all/export')
def export_{api_info.code}(request):
    export_fields = ({field_code})
    return export_data(request, {RuleConvert.to_upper_camel_case(api_info.code)}, {RuleConvert.to_upper_camel_case(api_info.code)}SchemaOut, export_fields)


# 导出
@router.post('/{api_info.code}/all/import')
def import_{api_info.code}(request, data: ImportSchema):
    import_fields = ({field_code})
    return import_data(request, {RuleConvert.to_upper_camel_case(api_info.code)}, {RuleConvert.to_upper_camel_case(api_info.code)}SchemaIn, data, import_fields)
    '''
    return api_txt
