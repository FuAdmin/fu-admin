/**
 * -*- coding: utf-8 -*-
 * time: 2022/5/4 01:13
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';

export const columns: BasicColumn[] = [
  {
    title: '文件名称',
    dataIndex: 'name',
    width: 100,
  },
  {
    title: '保存名称',
    dataIndex: 'save_name',
    width: 100,
  },
  {
    title: '文件大小',
    dataIndex: 'size',
    width: 100,
  },
  {
    title: 'URL',
    dataIndex: 'url',
    width: 200,
  },
  {
    title: '创建时间',
    dataIndex: 'create_datetime',
    width: 100,
  },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'name',
    label: '文件名称',
    component: 'Input',
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
    label: '文件名称',
    required: false,
    component: 'Input',
  },
  {
    field: 'size',
    label: '文件大小',
    required: false,
    component: 'Input',
  },
  {
    field: 'save_name',
    label: '保存名称',
    required: false,
    component: 'Input',
  },
  {
    field: 'url',
    label: 'URL',
    required: false,
    component: 'Input',
  },
];
