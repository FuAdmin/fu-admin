/**
 * -*- coding: utf-8 -*-
 * time: 2022/5/26 23:54
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';

export const columns: BasicColumn[] = [
  {
    title: '项目名称',
    dataIndex: 'name',
    width: 200,
  },
  {
    title: '项目编码',
    dataIndex: 'code',
    width: 180,
  },
  {
    title: '项目排序',
    dataIndex: 'sort',
    width: 100,
  },
  {
    title: '项目状态',
    dataIndex: 'status',
    width: 100,
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
    label: '项目名称',
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
    field: 'name',
    label: '项目名称',
    required: true,
    component: 'Input',
  },
  {
    field: 'code',
    label: '项目编码',
    required: true,
    component: 'Input',
  },
  {
    field: 'status',
    component: 'DictSelect',
    label: '项目状态',
    componentProps: {
      dictCode: 'project_status',
    },
  },
  {
    field: 'sort',
    label: '岗位排序',
    component: 'InputNumber',
    required: true,
  },
];
