import json


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
    form_schemas = ''
    form_info = json.loads(data_info.form_info).get('schemas')
    for item in form_info:
        form_schema = f'''
  {{
    component: '{item['component']}',
    label: '{item['label']}',
    colProps: {{
      span: {item['colProps']['span']}
    }},
    field: '{item['field']}',
  }},
'''
        form_schemas = form_schemas + form_schema
    form_txt = f'''export const formSchema: FormSchema[] = [
  {{
    field: 'id',
    label: 'id',
    component: 'Input',
    show: false,
  }},
{form_schemas}
]
'''

    return head_txt + column_txt + search_txt + form_txt
