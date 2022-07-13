/**
 * -*- coding: utf-8 -*-
 * time: 2022/4/01 22:54
 * author: 臧成龙
 * QQ: 939589097
 */

import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { h } from 'vue';
import { Tag, Image } from 'ant-design-vue';
import { rules } from '/@/utils/helper/validator';
import { getAllList } from '/@/views/fuadmin/system/role/role.api';
import { getAllList as getPostAllList } from '/@/views/fuadmin/system/post/post.api';

export const columns: BasicColumn[] = [
  {
    title: '用户名',
    dataIndex: 'username',
    width: 120,
  },
  {
    title: '姓名',
    dataIndex: 'name',
    width: 120,
  },
  {
    title: '头像',
    dataIndex: 'avatar',
    width: 80,
    customRender: ({ record }) => {
      const avatar = record.avatar;
      return h(Image, { src: avatar, width: 40 });
    },
  },
  {
    title: '邮箱',
    dataIndex: 'email',
    width: 120,
  },
  {
    title: '电话',
    dataIndex: 'mobile',
    width: 120,
  },
  {
    title: '性别',
    dataIndex: 'gender',
    width: 80,
    customRender: ({ record }) => {
      const gender = record.gender;
      // const enable = ~~status === 1;
      const color = gender ? 'cyan' : 'purple';
      const text = gender ? '男' : '女';
      return h(Tag, { color: color }, () => text);
    },
  },
  {
    title: '状态',
    dataIndex: 'status',
    width: 80,
    customRender: ({ record }) => {
      const status = record.status;
      const enable = ~~status === 1;
      const color = enable ? 'success' : 'error';
      const text = enable ? '启用' : '停用';
      return h(Tag, { color: color }, () => text);
    },
  },
  {
    title: '创建时间',
    dataIndex: 'create_datetime',
    width: 180,
  },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'name',
    label: '用户姓名',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'mobile',
    label: '用户电话',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'status',
    label: '用户状态',
    component: 'Select',
    componentProps: {
      options: [
        { label: '启用', value: true },
        { label: '停用', value: false },
      ],
    },
    colProps: { span: 6 },
  },
];

export const accountFormSchema: FormSchema[] = [
  {
    field: 'id',
    label: 'id',
    component: 'Input',
    show: false,
  },
  {
    field: 'password',
    label: 'password',
    component: 'Input',
    show: false,
  },
  {
    field: 'username',
    label: '用户账号',
    component: 'Input',
    required: true,
  },
  {
    field: 'name',
    label: '用户姓名',
    component: 'Input',
    required: true,
  },

  {
    field: 'mobile',
    label: '用户电话',
    component: 'Input',
    rules: rules.rule('phone', false),
  },
  {
    field: 'email',
    label: '用户邮箱',
    component: 'Input',
    rules: rules.rule('email', false),
  },
  {
    label: '用户角色',
    field: 'role',
    component: 'ApiSelect',
    componentProps: {
      api: getAllList,
      labelField: 'name',
      valueField: 'id',
      mode: 'multiple',
    },
    required: true,
  },
  {
    label: '用户岗位',
    field: 'post',
    component: 'ApiSelect',
    componentProps: {
      api: getPostAllList,
      labelField: 'name',
      valueField: 'id',
      mode: 'multiple',
    },
    required: true,
  },
  {
    field: 'dept',
    label: '所属部门',
    component: 'TreeSelect',
    componentProps: {
      fieldNames: {
        label: 'name',
        key: 'id',
        value: 'id',
      },
      getPopupContainer: () => document.body,
    },
    required: true,
  },
  {
    field: 'gender',
    label: '用户性别',
    component: 'RadioButtonGroup',
    defaultValue: 1,
    componentProps: {
      options: [
        { label: '男', value: 1 },
        { label: '女', value: 0 },
      ],
    },
  },
  {
    field: 'status',
    label: '部门状态',
    component: 'RadioButtonGroup',
    defaultValue: true,
    componentProps: {
      options: [
        { label: '启用', value: true },
        { label: '停用', value: false },
      ],
    },
    required: true,
  },

  {
    field: 'avatar',
    label: '用户头像',
    component: 'Input',
    slot: 'avatar',
  },
];
