from django.db import models
from utils.models import CoreModel   


class TemplateTest(CoreModel):
        
    input_text_area_2 = models.TextField(null=True, blank=True, verbose_name='文本域', help_text='文本域')    
    input_1 = models.CharField(null=True, blank=True, max_length=255, verbose_name='输入框', help_text='输入框')

    class Meta:
        db_table = 'generator_template_test'
        verbose_name = '测试1'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)
    