/**
 * -*- coding: utf-8 -*-
 * time: 2022/4/22 23:51
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { getIntervalData } from '/@/views/fuadmin/system/celery/util';

export const columns: BasicColumn[] = [
  {
    title: '',
    dataIndex: 'every',
    width: 300,
    customRender: ({ record }) => {
      return getIntervalData(record);
    },
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
    field: 'every',
    label: '频率',
    component: 'InputNumber',
    defaultValue: 1,
    required: true,
  },
  {
    field: 'period',
    label: '周期',
    component: 'Select',
    defaultValue: 'days',
    componentProps: {
      options: [
        { label: '天', value: 'days' },
        { label: '小时', value: 'hours' },
        { label: '分钟', value: 'minutes' },
        { label: '秒', value: 'seconds' },
      ],
    },
  },
];
