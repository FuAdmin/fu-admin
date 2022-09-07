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
import { useI18n } from '/@/hooks/web/useI18n';
const { t } = useI18n();

export const columns: BasicColumn[] = [
  {
    title: t('common.task.taskText'),
    dataIndex: 'task',
    width: 200,
  },
  {
    title: t('common.task.nameText'),
    dataIndex: 'name',
    width: 180,
  },
  {
    title: t('common.task.intervalText'),
    dataIndex: 'interval',
    width: 100,
    customRender: ({ record }) => {
      return getIntervalData(record.interval);
    },
  },
  {
    title: t('common.task.crontabText'),
    dataIndex: 'crontab',
    width: 100,
    customRender: ({ record }) => {
      return getCrontabData(record.crontab);
    },
  },
  {
    title: t('common.statusText'),
    dataIndex: 'enabled',
    width: 100,
    customRender: ({ record }) => {
      const status = record.enabled;
      const color = status ? 'success' : 'error';
      const text = status ? t('common.enableText') : t('common.disableText');
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
    label: t('common.task.taskText'),
    required: true,
    component: 'Input',
  },
  {
    field: 'name',
    label: t('common.task.nameText'),
    required: true,
    component: 'Input',
  },
  {
    field: 'interval',
    label: t('common.task.intervalText'),
    component: 'Select',
  },
  {
    field: 'crontab',
    label: t('common.task.crontabText'),
    component: 'Select',
  },
  {
    field: 'enabled',
    label: t('common.statusText'),
    component: 'RadioButtonGroup',
    defaultValue: true,
    componentProps: {
      options: [
        { label: t('common.enableText'), value: true },
        { label: t('common.disableText'), value: false },
      ],
    },
  },
];
