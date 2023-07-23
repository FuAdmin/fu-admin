import json

from system.code_template.backend.mapping import component_to_db_type
from utils.ru_convert import RuleConvert


def generator_backend_model(model_info):
    form_info = model_info.form_info
    form_info_dict = json.loads(form_info)
    header_txt = f'''from django.db import models
from utils.models import CoreModel   


'''
    columns_txt = ''
    for item in form_info_dict.get('schemas'):
        column = f'''    
    {item['field']} = models.{component_to_db_type[item['component']]}verbose_name='{item['label']}', help_text='{item['label']}')'''
        columns_txt = column + columns_txt

    bottom_txt = f'''class {RuleConvert.to_upper_camel_case(model_info.code)}(CoreModel):
    {columns_txt}

    class Meta:
        db_table = 'generator_{model_info.code}'
        verbose_name = '{model_info.name}'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)
    '''
    model_txt = header_txt + bottom_txt
    return model_txt
