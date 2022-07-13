/**
 * -*- coding: utf-8 -*-
 * time: 2022/4/3 23:58
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { h } from 'vue';
import { Tag } from 'ant-design-vue';

export const columns: BasicColumn[] = [
  {
    title: '按钮名称',
    dataIndex: 'name',
    width: 200,
  },
  {
    title: '按钮编码',
    dataIndex: 'code',
    width: 180,
  },
  {
    title: '按钮排序',
    dataIndex: 'sort',
    width: 100,
  },
  {
    title: '按钮状态',
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
    title: '按钮备注',
    dataIndex: 'remark',
  },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'name',
    label: '按钮名称',
    component: 'Input',
    colProps: { span: 8 },
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
    colProps: { span: 8 },
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
    label: '按钮名称',
    required: true,
    component: 'Input',
  },
  {
    field: 'code',
    label: '按钮编码',
    required: true,
    component: 'Input',
  },
  {
    field: 'status',
    label: '按钮状态',
    component: 'RadioButtonGroup',
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
    label: '按钮排序',
    component: 'InputNumber',
    required: true,
  },
  {
    label: '按钮备注',
    field: 'remark',
    component: 'InputTextArea',
  },
];
