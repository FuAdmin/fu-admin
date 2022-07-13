/**
 * -*- coding: utf-8 -*-
 * time: 2022/4/8 01:12
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';

export const columns: BasicColumn[] = [
  {
    title: '显示值',
    dataIndex: 'label',
    width: 160,
    align: 'left',
  },
  {
    title: '实际值',
    dataIndex: 'value',
    width: 180,
  },
  {
    title: '编码',
    dataIndex: 'code',
    width: 180,
  },
  {
    title: '排序',
    dataIndex: 'sort',
    width: 50,
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
    field: 'label',
    label: '显示值',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'value',
    label: '实际值',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'code',
    label: '编码',
    component: 'Input',
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
    label: '上级字典',
    component: 'TreeSelect',
    componentProps: {
      fieldNames: {
        label: 'label',
        key: 'id',
        value: 'id',
      },
      getPopupContainer: () => document.body,
    },
  },

  {
    field: 'label',
    label: '显示值',
    component: 'Input',
    required: true,
  },
  {
    field: 'value',
    label: '实际值',
    component: 'Input',
    required: true,
  },
  {
    field: 'code',
    label: '编码',
    component: 'Input',
    required: true,
  },

  {
    field: 'sort',
    label: '排序',
    defaultValue: 1,
    component: 'InputNumber',
    required: true,
  },
  {
    label: '备注',
    field: 'remark',
    component: 'InputTextArea',
  },
];
