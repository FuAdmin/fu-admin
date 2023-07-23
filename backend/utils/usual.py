# -*- coding: utf-8 -*-
# @Time    : 2022/6/4 23:32
# @Author  : 臧成龙
# @FileName: usual.py
# @Software: PyCharm
# -*- coding: utf-8 -*-

from fuadmin.settings import SECRET_KEY
from system.models import Dept

from .fu_jwt import FuJwt


def get_user_info_from_token(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    token = token.split(" ")[1]
    jwt = FuJwt(SECRET_KEY)
    value = jwt.decode(SECRET_KEY, token)
    user_info = value.payload
    return user_info


def get_dept(dept_id: int, dept_all_list=None, dept_list=None):
    """
    递归获取部门的所有下级部门
    :param dept_id: 需要获取的部门id
    :param dept_all_list: 所有部门列表
    :param dept_list: 递归部门list
    :return:
    """
    if not dept_all_list:
        dept_all_list = Dept.objects.all().values('id', 'parent')
    if dept_list is None:
        dept_list = [dept_id]
    for ele in dept_all_list:
        if ele.get('parent') == dept_id:
            dept_list.append(ele.get('id'))
            get_dept(ele.get('id'), dept_all_list, dept_list)
    return list(set(dept_list))


def insert_content_after_line(filename, target_line, content_to_insert):
    try:
        # 打开文件并读取内容
        with open(filename, 'r') as file:
            lines = file.readlines()

        # 找到目标行的索引位置
        target_line_index = None
        for i, line in enumerate(lines):
            if target_line in line:
                target_line_index = i
                break

        if target_line_index is not None:
            # 在目标行后面插入内容
            lines.insert(target_line_index + 1, content_to_insert + '\n')

            # 将更新后的内容写回文件中
            with open(filename, 'w') as file:
                file.writelines(lines)
            print("内容已成功插入到目标行后。")
        else:
            print("未找到目标行。")

    except FileNotFoundError:
        print(f"文件 '{filename}' 未找到。")
