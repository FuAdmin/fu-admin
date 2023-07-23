from django.db import models
from utils.models import CoreModel   


class TestDemo(CoreModel):
        
    des = models.TextField(null=True, blank=True, verbose_name='描述', help_text='描述')    
    code = models.DecimalField(null=True, blank=True, max_digits = 13, decimal_places = 4, verbose_name='编码', help_text='编码')    
    name = models.CharField(null=True, blank=True, max_length=255, verbose_name='名称', help_text='名称')

    class Meta:
        db_table = 'generator_test_demo'
        verbose_name = '测试案例'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)
    