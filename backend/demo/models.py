from django.db import models
from utils.models import CoreModel


class Demo(CoreModel):
    name = models.CharField(null=False, max_length=64, verbose_name="项目名称", help_text="项目名称")
    code = models.CharField(max_length=32, verbose_name="项目编码", help_text="项目编码")
    status = models.CharField(max_length=64, verbose_name="项目状态", help_text="项目状态")

    class Meta:
        db_table = "Demo"
        verbose_name = '项目演示'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)
