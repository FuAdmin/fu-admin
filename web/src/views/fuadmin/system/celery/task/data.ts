/**
 * -*- coding: utf-8 -*-
 * time: 2022/4/26 23:41
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { h } from 'vue';
import { Tag } from 'ant-design-vue';
import { getCrontabData, getIntervalData } from '/@/views/fuadmin/system/celery/util';

export const columns: BasicColumn[] = [
  {
    title: '任务',
    dataIndex: 'task',
    width: 200,
  },
  {
    title: '名称',
    dataIndex: 'name',
    width: 180,
  },
  {
    title: '任务频率',
    dataIndex: 'interval',
    width: 100,
    customRender: ({ record }) => {
      return getIntervalData(record.interval);
    },
  },
  {
    title: '任务定时',
    dataIndex: 'crontab',
    width: 100,
    customRender: ({ record }) => {
      return getCrontabData(record.crontab);
    },
  },
  {
    title: '任务状态',
    dataIndex: 'enabled',
    width: 100,
    customRender: ({ record }) => {
      const status = record.enabled;
      const color = status ? 'success' : 'error';
      const text = status ? '开启' : '关闭';
      return h(Tag, { color: color }, () => text);
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
    field: 'task',
    label: '任务',
    required: true,
    component: 'Input',
  },
  {
    field: 'name',
    label: '名称',
    required: true,
    component: 'Input',
  },
  {
    field: 'interval',
    label: '任务频率',
    component: 'Select',
  },
  {
    field: 'crontab',
    label: '任务定时',
    component: 'Select',
  },
  {
    field: 'enabled',
    label: '任务状态',
    component: 'RadioButtonGroup',
    defaultValue: true,
    componentProps: {
      options: [
        { label: '开启', value: true },
        { label: '关闭', value: false },
      ],
    },
  },
];
