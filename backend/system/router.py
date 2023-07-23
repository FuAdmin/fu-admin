# -*- coding: utf-8 -*-
# @Time    : 2022/5/10 00:02
# @Author  : 臧成龙
# @FileName: router.py
# @Software: PyCharm

from ninja import Router
from system.apis.dept import router as dept_router
from system.apis.post import router as post_router
from system.apis.login import router as login_router
from system.apis.menu import router as menu_router
from system.apis.role import router as role_router
from system.apis.button import router as button_router
from system.apis.menu_button import router as menu_button_router
from system.apis.user import router as user_router
from system.apis.data_dict.dict import router as dict_router
from system.apis.data_dict.dict_item import router as dict_item_router
from system.apis.data_dict.category_dict import router as category_dict_router
from system.apis.log.login_log import router as login_log_router
from system.apis.log.operation_log import router as operation_log_router
from system.apis.celery_crontab import router as celery_crontab_router
from system.apis.celery_interval import router as celery_interval_router
from system.apis.celery_periodic import router as celery_periodic_router
from system.apis.log.celery_log import router as celery_log_router
from system.apis.file import router as file_router
from system.apis.monitor import router as monitor_router
from system.apis.menu_column import router as menu_column_field_router
from system.apis.code_generator import router as generator_template_router

system_router = Router()
system_router.add_router('/', dept_router, tags=["Dept"])
system_router.add_router('/', post_router, tags=["Post"])
system_router.add_router('/', login_router, tags=["Login"])
system_router.add_router('/', menu_router, tags=["Menu"])
system_router.add_router('/', role_router, tags=["Role"])
system_router.add_router('/', button_router, tags=["Button"])
system_router.add_router('/', menu_button_router, tags=["MenuButton"])
system_router.add_router('/', user_router, tags=["User"])
system_router.add_router('/', dict_router, tags=["Dict"])
system_router.add_router('/', dict_item_router, tags=["DictItem"])
system_router.add_router('/', category_dict_router, tags=["CategoryDict"])
system_router.add_router('/', login_log_router, tags=["LoginLog"])
system_router.add_router('/', operation_log_router, tags=["OperationLog"])
system_router.add_router('/', celery_crontab_router, tags=["CeleryCrontab"])
system_router.add_router('/', celery_interval_router, tags=["CeleryInterval"])
system_router.add_router('/', celery_periodic_router, tags=["CeleryPeriodic"])
system_router.add_router('/', celery_log_router, tags=["CeleryLog"])
system_router.add_router('/', file_router, tags=["File"])
system_router.add_router('/', monitor_router, tags=["Monitor"])
system_router.add_router('/', menu_column_field_router, tags=["MenuColumnField"])
system_router.add_router('/', generator_template_router, tags=["GeneratorTemplate"])
