from django.db import models
from utils.models import CoreModel   


class Fd(CoreModel):
        
    select_1 = models.CharField(null=True, blank=True, max_length=255, verbose_name='下拉选择', help_text='下拉选择')    
    input_number_2 = models.DecimalField(null=True, blank=True, max_digits = 13, decimal_places = 4, verbose_name='数字输入框', help_text='数字输入框')    
    input_1 = models.CharField(null=True, blank=True, max_length=255, verbose_name='输入框', help_text='输入框')

    class Meta:
        db_table = 'generator_fd'
        verbose_name = 'fd'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)
    