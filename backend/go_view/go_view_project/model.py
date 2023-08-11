from django.db import models
from utils.models import CoreModel   


class GoViewProject(CoreModel):
        
    index_image = models.CharField(null=True, blank=True, max_length=255, verbose_name='index_image', help_text='index_image')    
    state = models.IntegerField(null=True, blank=True, verbose_name='state', help_text='state')
    project_name = models.CharField(null=True, blank=True, max_length=255, verbose_name='project_name', help_text='project_name')
    content = models.TextField(null=True, blank=True, verbose_name='content', help_text='content')

    class Meta:
        db_table = 'go_view_project'
        verbose_name = 'Go View Project'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)
    