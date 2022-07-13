/**
 * -*- coding: utf-8 -*-
 * time: 2022/4/28 23:34
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { h } from 'vue';
import { Tag } from 'ant-design-vue';

export const columns: BasicColumn[] = [
  {
    title: '显示名称',
    dataIndex: 'label',
    width: 50,
  },
  {
    title: '实际值',
    dataIndex: 'value',
    width: 70,
  },
  {
    title: '状态',
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
    width: 120,
    ifShow: false,
  },
  {
    title: '备注',
    dataIndex: 'remark',
    ifShow: false,
  },
];

// @ts-ignore
// @ts-ignore
export const formSchema: FormSchema[] = [
  {
    field: 'id',
    label: 'id',
    component: 'Input',
    show: false,
  },
  {
    field: 'label',
    label: '显示名称',
    component: 'Input',
    required: true,
  },
  {
    field: 'value',
    label: '实际值',
    required: true,
    component: 'Input',
    show: true,
  },
  {
    field: 'status',
    label: '状态',
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
    label: '排序',
    component: 'InputNumber',
    defaultValue: 1,
    required: true,
  },
  {
    label: '备注',
    field: 'remark',
    component: 'InputTextArea',
  },
];
