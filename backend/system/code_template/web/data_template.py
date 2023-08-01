import json
import re


# 自定义函数用于处理布尔值转换
def bool_to_str(val):
    if isinstance(val, bool):
        return str(val).lower()  # 将布尔值转换为小写字符串
    raise TypeError("Object of type %s is not JSON serializable" % type(val))


# Custom JSON decoder to convert boolean strings to boolean values
def custom_json_decoder(data):
    for key, value in data.items():
        if value == 'true':
            data[key] = True
        elif value == 'false':
            data[key] = False
    return data


def generator_data(data_info):
    head_txt = f'''
import {{ BasicColumn }} from '/@/components/Table';
import {{ FormSchema }} from '/@/components/Table';
'''
    column_schemas = ''
    table_info = json.loads(data_info.table_info)
    column_info = table_info.get('columnInfo')
    for item in column_info:
        column_schema = f'''
  {{
    title: '{item['column_name']}',
    dataIndex: '{item['field_name']}',
    width: '{item['width']}',
    fixed: '{item['freeze']}',
    align: '{item['align']}',
    auth: ['{data_info.code + ':' + item['field_name']}'],
    resizable: {str(item['resizable']).lower()},
  }},
'''
        column_schemas = column_schemas + column_schema
    column_txt = f'''export const columns: BasicColumn[] = [
    {column_schemas}
]
'''

    search_schemas = ''
    table_info = json.loads(data_info.table_info)
    search_info = table_info.get('searchInfo')
    for item in search_info:
        search_schema = f'''
  {{
    label: '{item['column_name']}',
    field: '{item['field_name']}',
    component: 'Input',
    colProps: {{ span: 6 }},
  }},
'''
        search_schemas = search_schemas + search_schema
    search_txt = f'''export const searchFormSchema: FormSchema[] = [
        {search_schemas}
];
'''
    form_info = json.loads(data_info.form_info).get('schemas')
    for item in form_info:
        item.pop('key')
        item.pop('icon')

    id_dict = {
        'field': 'id',
        'label': 'id',
        'component': 'Input',
        'show': False,
    }
    form_info.insert(0, id_dict)

    json_str = json.dumps(form_info, ensure_ascii=False, indent=2, default=bool_to_str)
    js_object = re.sub(r'"\b(\w+)\b":', r'\1:', json_str)
    form_schemas = js_object.replace('"', "'")

    form_txt = f'''export const formSchema: FormSchema[] = {form_schemas}'''

    return head_txt + column_txt + search_txt + form_txt
