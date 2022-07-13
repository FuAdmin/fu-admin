/**
 * -*- coding: utf-8 -*-
 * time: 2022/4/29 01:37
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { h } from 'vue';
import { Tag } from 'ant-design-vue';

export const columns: BasicColumn[] = [
  {
    title: '字典名称',
    dataIndex: 'name',
    width: 200,
  },
  {
    title: '字典编码',
    dataIndex: 'code',
    width: 180,
  },
  {
    title: '字典排序',
    dataIndex: 'sort',
    width: 100,
  },
  {
    title: '字典状态',
    dataIndex: 'status',
    width: 100,
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
  {
    title: '字典备注',
    dataIndex: 'remark',
  },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'name',
    label: '按钮名称',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'status',
    label: '按钮状态',
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
    field: 'name',
    label: '字典名称',
    required: true,
    component: 'Input',
  },
  {
    field: 'code',
    label: '字典编码',
    required: true,
    component: 'Input',
  },
  {
    field: 'status',
    label: '字典状态',
    component: 'RadioButtonGroup',
    required: true,
    defaultValue: true,
    componentProps: {
      options: [
        { label: '启用', value: true },
        { label: '停用', value: false },
      ],
    },
  },
  {
    field: 'sort',
    label: '字典排序',
    component: 'InputNumber',
    required: true,
  },
  {
    label: '字典备注',
    field: 'remark',
    component: 'InputTextArea',
  },
];
