/**
 * -*- coding: utf-8 -*-
 * time: 2022/5/26 23:54
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { h } from 'vue';
import { Tag } from 'ant-design-vue';

export const columns: BasicColumn[] = [
  {
    title: '岗位名称',
    dataIndex: 'name',
    width: 200,
  },
  {
    title: '岗位编码',
    dataIndex: 'code',
    width: 180,
  },
  {
    title: '岗位排序',
    dataIndex: 'sort',
    width: 100,
  },
  {
    title: '岗位状态',
    dataIndex: 'status',
    width: 100,
    customRender: ({ record }) => {
      const status = record.status;
      const enable = ~~status === 1;
      const color = enable ? 'success' : 'error';
      const text = enable ? '在职' : '离职';
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
    label: '岗位名称',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'status',
    label: '岗位状态',
    component: 'Select',
    componentProps: {
      options: [
        { label: '在职', value: 1 },
        { label: '离职', value: 0 },
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
    label: '岗位名称',
    required: true,
    component: 'Input',
  },
  {
    field: 'code',
    label: '岗位编码',
    required: true,
    component: 'Input',
  },
  // {
  //   field: 'field',
  //   component: 'DictSelect',
  //   label: '字段',
  //   componentProps: {
  //     dictCode: 'status',
  //   },
  // },
  {
    field: 'status',
    label: '岗位状态',
    component: 'RadioButtonGroup',
    defaultValue: 1,
    componentProps: {
      options: [
        { label: '在职', value: 1 },
        { label: '离职', value: 0 },
      ],
    },
  },
  {
    field: 'sort',
    label: '岗位排序',
    component: 'InputNumber',
    required: true,
  },
];
