/**
 * -*- coding: utf-8 -*-
 * time: 2022/4/12 22:53
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { getCrontabData } from '/@/views/fuadmin/system/celery/util';

export const columns: BasicColumn[] = [
  {
    title: '',
    dataIndex: 'code',
    width: 300,
    customRender: ({ record }) => {
      return getCrontabData(record);
    },
  },
];

export const formSchema: FormSchema[] = [
  {
    field: 'id',
    label: 'id',
    defaultValue: '*',
    component: 'Input',
    show: false,
  },
  {
    field: 'minute',
    label: '分钟',
    defaultValue: '*',
    required: true,
    component: 'Input',
  },
  {
    field: 'hour',
    label: '小时',
    defaultValue: '*',
    required: true,
    component: 'Input',
  },
  {
    field: 'day_of_week',
    label: '每周的周几',
    defaultValue: '*',
    required: true,
    component: 'Input',
  },
  {
    field: 'day_of_month',
    label: '每月的某天',
    defaultValue: '*',
    required: true,
    component: 'Input',
  },
  {
    field: 'month_of_year',
    label: '每年的某月',
    defaultValue: '*',
    required: true,
    component: 'Input',
  },
];
