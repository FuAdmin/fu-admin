/**
 * -*- coding: utf-8 -*-
 * time: 2022/5/3 22:12
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { h } from 'vue';
import { Tag } from 'ant-design-vue';
import { rules } from '/@/utils/helper/validator';

export const columns: BasicColumn[] = [
  {
    title: '部门名称',
    dataIndex: 'name',
    width: 160,
    align: 'left',
  },
  {
    title: '部门电话',
    dataIndex: 'phone',
    width: 180,
  },
  {
    title: '部门邮箱',
    dataIndex: 'email',
    width: 180,
  },
  {
    title: '排序',
    dataIndex: 'sort',
    width: 50,
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
    title: '备注',
    dataIndex: 'remark',
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
    label: '部门名称',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'status',
    label: '状态',
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

export const formSchema: FormSchema[] = [
  {
    field: 'id',
    label: 'id',
    component: 'Input',
    show: false,
  },
  {
    field: 'parent_id',
    label: '上级部门',
    component: 'TreeSelect',
    componentProps: {
      fieldNames: {
        label: 'name',
        key: 'id',
        value: 'id',
      },
      getPopupContainer: () => document.body,
    },
  },

  {
    field: 'name',
    label: '部门名称',
    component: 'Input',
    required: true,
  },
  {
    field: 'phone',
    label: '部门电话',
    component: 'Input',
    rules: rules.rule('phone', false),
  },
  {
    field: 'email',
    label: '部门邮箱',
    component: 'Input',
    rules: rules.rule('email', false),
  },

  {
    field: 'sort',
    label: '部门排序',
    component: 'InputNumber',
    required: true,
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
    label: '部门备注',
    field: 'remark',
    component: 'InputTextArea',
  },
];
