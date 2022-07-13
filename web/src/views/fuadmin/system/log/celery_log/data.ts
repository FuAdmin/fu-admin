/**
 * -*- coding: utf-8 -*-
 * time: 2022/5/7 23:37
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';

export const columns: BasicColumn[] = [
  {
    title: '任务ID',
    dataIndex: 'task_id',
    width: 100,
  },
  {
    title: '任务',
    dataIndex: 'task_name',
    width: 100,
  },
  {
    title: '名称',
    dataIndex: 'periodic_task_name',
    width: 100,
  },
  {
    title: '状态',
    dataIndex: 'status',
    width: 100,
  },
  {
    title: '结果',
    dataIndex: 'result',
    width: 150,
  },
  {
    title: '创建时间',
    dataIndex: 'date_created',
    width: 100,
  },
  {
    title: '完成时间',
    dataIndex: 'date_done',
    width: 100,
  },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'periodic_task_name',
    label: '名称',
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
    field: 'task_id',
    label: '任务ID',
    required: false,
    component: 'Input',
  },
  {
    field: 'task_name',
    label: '任务',
    required: false,
    component: 'Input',
  },
  {
    field: 'periodic_task_name',
    label: '名称',
    required: false,
    component: 'Input',
  },
  {
    field: 'status',
    label: '状态',
    required: false,
    component: 'Input',
  },
  {
    field: 'result',
    label: '结果',
    required: false,
    component: 'Input',
  },
  {
    field: 'date_created',
    label: '创建时间',
    required: false,
    component: 'Input',
  },
  {
    field: 'date_done',
    label: '完成时间',
    required: false,
    component: 'Input',
  },
];
