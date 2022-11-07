from flow.loon_base_model import BaseModel
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from system.models import Users, Dept


class LoonUserDept(BaseModel):
    """
    用户部门
    """
    user = models.ForeignKey(Users, to_field='id', db_constraint=False, on_delete=models.DO_NOTHING)
    dept = models.ForeignKey(Dept, to_field='id', db_constraint=False, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "loon_user_dept"
        verbose_name = '用户部门表'
        verbose_name_plural = verbose_name
        ordering = ('-gmt_created',)


class LoonUserRole(BaseModel):
    """
    用户角色
    """
    user_id = models.IntegerField('用户id')
    role_id = models.IntegerField('角色id')

    class Meta:
        db_table = "loon_user_role"
        verbose_name = '用户角色表'
        verbose_name_plural = verbose_name
        ordering = ('-gmt_created',)


class AppToken(BaseModel):
    """
    App token,用于api调用方授权
    """
    app_name = models.CharField('应用名称', max_length=50)
    token = models.CharField('签名令牌', max_length=50, help_text='后端自动生成')
    ticket_sn_prefix = models.CharField('工单流水号前缀', default='loonflow', max_length=20, help_text='工单流水号前缀，如设置为loonflow,则创建的工单的流水号为loonflow_201805130013')

    def get_dict(self):
        role_dict_info = super().get_dict()
        creator_obj = Users.objects.filter(username=getattr(self, 'creator')).first()
        if creator_obj:
            role_dict_info['creator_info'] = dict(creator_id=creator_obj.id, creator_alias=creator_obj.name,
                                                  creator_username=creator_obj.username)
        else:
            role_dict_info['creator_info'] = dict(creator_id=0, creator_alias='', creator_username=getattr(self, 'creator'))
        return role_dict_info


    class Meta:
        db_table = "loon_app_token"
        verbose_name = '用户部门表'
        verbose_name_plural = verbose_name
        ordering = ('-gmt_created',)