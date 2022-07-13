import json
import logging
import os
import shutil

from django.core.management.base import BaseCommand

from fuadmin.settings import BASE_DIR

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    创建App命令:
    python manage.py createapp app名
    python manage.py createapp app01 app02 ...
    python manage.py createapp 一级文件名/app01 ...    # 支持多级目录建app
    """

    def add_arguments(self, parser):
        parser.add_argument('app_info', nargs='*', type=str, )

    def handle(self, *args, **options):
        app_info = options.get('app_info')
        for name in app_info:
            app = json.loads(name)
            name = app.get('app_name')
            names = name.split('/')
            dnames = ".".join(names)
            app_path = os.path.join(BASE_DIR, "dvadmin", *names)
            # 判断app是否存在
            if os.path.exists(app_path):
                print(f"App {name} 已存在！")
                # break
            else:
                source_path = os.path.join(BASE_DIR, "dvadmin", "utils", "template")
                target_path = app_path
                if not os.path.exists(target_path):
                    # 如果目标路径不存在原文件夹的话就创建
                    os.makedirs(target_path)
                if os.path.exists(source_path):
                    # 如果目标路径存在原文件夹的话就先删除
                    shutil.rmtree(target_path)
                shutil.copytree(source_path, target_path)
                # 注册app到 settings.py 中
                injection(os.path.join(BASE_DIR, "application", "settings.py"), f"    'dvadmin.{dnames}',\n",
                          "INSTALLED_APPS",
                          "]")

                # 注册app到 urls.py 中
                injection(os.path.join(BASE_DIR, "application", "urls.py"),
                          f"    path(r'api/{name}/', include('dvadmin.{dnames}.urls')),\n", "urlpatterns = [",
                          "]")

            # 修改app中的apps 内容
            app_content = f"""
from django.apps import AppConfig


class {name.capitalize()}Config(AppConfig):
    name = 'dvadmin.{dnames}'
    verbose_name = "{names[-1]}App"
"""
            with open(os.path.join(app_path, "apps.py"), 'w', encoding='UTF-8') as f:
                f.write(app_content)

            # 修改Model的内容

            table_name = app.get('table_name')
            model_name = app.get('model_name')

            # app中所有不重复的字段
            app_fields = app.get('fields')
            field_content = ''
            # app中所有不重复的字段type
            fields_type = set()
            # app中所有的字段name
            fields_name = set()
            for field in app_fields:
                fields_type.add(field['type'])
                fields_name.add(field['name'])
                if field['type'] == 'CharField':
                    field_content = f"""{field_content}
    {field['name']} = {field['type']}(max_length={field['max_length']}, verbose_name='{field['name']}', help_text='{field['description']}')"""
                elif field['type'] == 'TextField':
                    field_content = f"""{field_content}
    {field['name']} = {field['type']}(verbose_name='{field['name']}', help_text='{field['description']}')"""
            model_content = f"""
from django.db.models import {','.join(fields_type)}
from dvadmin.utils.models import CoreModel


class {model_name}(CoreModel):
{field_content}

    class Meta:
        verbose_name = '{model_name}'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.{fields_name.pop()} 
"""

            with open(os.path.join(app_path, "models", f"{table_name}.py"), 'w', encoding='UTF-8') as f:
                f.write(model_content)

            # 修改 model init文件
            model_init_content = f"from dvadmin.{name}.models.{table_name} import {model_name}"
            with open(os.path.join(app_path, "models", "__init__.py"), 'a', encoding='UTF-8') as f:
                f.write(model_init_content)
                f.write('\n')

            # 修改filters的内容
            filter_content = f"""
import django_filters
from dvadmin.{name}.models import {model_name}


class {model_name}Filter(django_filters.rest_framework.FilterSet):

    # 通过 lookup_expr 可进行模糊查询，其他配置可自行百度
    # name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = {model_name}
        fields = '__all__'

"""
            with open(os.path.join(app_path, "filters", f"{table_name}_filter.py"), 'w', encoding='UTF-8') as f:
                f.write(filter_content)

            # 修改 filters init文件
            filter_init_content = f"from .{table_name}_filter import {model_name}Filter"
            with open(os.path.join(app_path, "filters", "__init__.py"), 'a', encoding='UTF-8') as f:
                f.write(filter_init_content)
                f.write('\n')

            # 修改serializers的内容
            serializer_content = f"""
from rest_framework import serializers
from dvadmin.{name}.models import {model_name}
from dvadmin.utils.serializers import CustomModelSerializer


class {model_name}Serializer(CustomModelSerializer):

    class Meta:
        model = {model_name}
        fields = '__all__'
        
        
class {model_name}CreateUpdateSerializer(CustomModelSerializer):

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = {model_name}
        fields = '__all__'


class {model_name}ImportSerializer(CustomModelSerializer):

    class Meta:
        model = {model_name}
        fields = '__all__'


class {model_name}ExportSerializer(CustomModelSerializer):

    class Meta:
        model = {model_name}
        fields = '__all__'

"""
            with open(os.path.join(app_path, 'serializers', f'{table_name}_serializer.py'), 'w', encoding='UTF-8') as f:
                f.write(serializer_content)

            # 修改 serializers init文件
            serializer_init_content = f"from .{table_name}_serializer import {model_name}Serializer, " \
                                      f"{model_name}CreateUpdateSerializer, " \
                                      f"{model_name}ImportSerializer, " \
                                      f"{model_name}ExportSerializer"
            with open(os.path.join(app_path, "serializers", "__init__.py"), 'a', encoding='UTF-8') as f:
                f.write(serializer_init_content)
                f.write('\n')
            # 修改view内容
            view_content = f"""
from dvadmin.utils.filters import DataLevelPermissionsFilter
from dvadmin.utils.viewset import CustomModelViewSet
from dvadmin.{name}.models import {model_name}
from dvadmin.{name}.filters import {model_name}Filter
from dvadmin.{name}.serializers import {model_name}Serializer, {model_name}CreateUpdateSerializer, {model_name}ImportSerializer, {model_name}ExportSerializer
                            
          
class {model_name}ModelViewSet(CustomModelViewSet):

    queryset = {model_name}.objects.all()
    serializer_class = {model_name}Serializer  # 序列化器
    create_serializer_class = {model_name}CreateUpdateSerializer  # 创建/更新时的列化器
    update_serializer_class = {model_name}CreateUpdateSerializer  # 创建/更新时的列化器
    filter_class = {model_name}Filter  # 过滤器
    extra_filter_backends = [DataLevelPermissionsFilter]  # 数据权限类，不需要可注释掉
    # ordering = ['create_datetime']  # 默认排序
    # 导出
    export_field_data = []  # 导出
    export_serializer_class = {model_name}ExportSerializer  # 导出序列化器
    # 导入
    import_field_data = []
    import_serializer_class = {model_name}ImportSerializer


"""
            with open(os.path.join(app_path, 'views', f'{table_name}_view.py'), 'w', encoding='UTF-8') as f:
                f.write(view_content)

            # 修改 views init文件
            view_init_content = f"from .{table_name}_view import {model_name}ModelViewSet"
            with open(os.path.join(app_path, "views", "__init__.py"), 'a', encoding='UTF-8') as f:
                f.write(view_init_content)
                f.write('\n')

            # 修改 url文件
            url_package = f"from dvadmin.{name}.views import {model_name}ModelViewSet"
            injection(os.path.join(app_path, "urls.py"),
                      f"{url_package}\n", "from rest_framework.routers import DefaultRouter",
                      "router = DefaultRouter()")

            url_path = f"router.register(r'{table_name}', {model_name}ModelViewSet)"
            injection(os.path.join(app_path, "urls.py"),
                      f"{url_path}\n", "router = DefaultRouter()",
                      "urlpatterns = [")

            export_import_url = f"""    # 导出项目
    path('{table_name}/export/', {model_name}ModelViewSet.as_view({{'get': 'export', }})),
    # 项目导入模板下载及导入
    path('{table_name}/importTemplate/', {model_name}ModelViewSet.as_view({{'get': 'importTemplate', 'post': 'importTemplate'}}))"""
            injection(os.path.join(app_path, "urls.py"),
                      f"{export_import_url}\n", "urlpatterns = [", "]")

            print(f"创建 {name} App成功")


def injection(file_path, insert_content, startswith, endswith):
    with open(file_path, "r+", encoding="utf-8") as f:
        data = f.readlines()
        with open(file_path, 'w', encoding='UTF-8') as f1:
            is_INSTALLED_APPS = False
            is_insert = False
            for content in data:
                # 判断文件是否 INSTALLED_APPS 开头
                if not is_insert and content.startswith(startswith):
                    is_INSTALLED_APPS = True
                if not is_insert and content.startswith(endswith) and is_INSTALLED_APPS:
                    # 给前一行插入数据
                    content = insert_content + content
                    is_insert = True
                f1.writelines(content)
