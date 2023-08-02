from django.db import models
from utils.models import CoreModel   


class GoViewData(CoreModel):
        
    content = models.TextField(null=True, blank=True, verbose_name='content', help_text='content')    
    project_id = models.IntegerField(null=True, blank=True, verbose_name='project_id', help_text='project_id')

    class Meta:
        db_table = 'go_view_data'
        verbose_name = 'Go View Data'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)
    