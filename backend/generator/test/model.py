from django.db import models
from utils.models import CoreModel   


class Test(CoreModel):
        
    icon = models.CharField(null=True, blank=True, max_length=255, verbose_name='图标', help_text='图标')    
    sequence = models.DecimalField(null=True, blank=True, max_digits = 13, decimal_places = 4, verbose_name='排序', help_text='排序')    
    code = models.CharField(null=True, blank=True, max_length=255, verbose_name='代码', help_text='代码')    
    name = models.CharField(null=True, blank=True, max_length=255, verbose_name='名称', help_text='名称')

    class Meta:
        db_table = 'generator_test'
        verbose_name = '模板测试'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)
    