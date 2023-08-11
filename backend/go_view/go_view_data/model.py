from django.db import models

from go_view.go_view_project.model import GoViewProject
from utils.models import CoreModel   


class GoViewData(CoreModel):
        
    content = models.TextField(null=True, blank=True, verbose_name='content', help_text='content')    
    # project_id = models.OneToOneField(to=GoViewProject, related_name='content', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'go_view_data'
        verbose_name = 'Go View Data'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)
    