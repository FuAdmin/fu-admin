/**
 * -*- coding: utf-8 -*-
 * time: 2022/4/22 23:51
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { getIntervalData } from '/@/views/fuadmin/system/celery/util';
import { useI18n } from '/@/hooks/web/useI18n';
const { t } = useI18n();

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
    label: t('common.task.everyText'),
    component: 'InputNumber',
    defaultValue: 1,
    required: true,
  },
  {
    field: 'period',
    label: t('common.task.periodText'),
    component: 'Select',
    defaultValue: 'days',
    componentProps: {
      options: [
        { label: t('common.task.dayText'), value: 'days' },
        { label: t('common.task.hourText'), value: 'hours' },
        { label: t('common.task.minuteText'), value: 'minutes' },
        { label: t('common.task.secondText'), value: 'seconds' },
      ],
    },
  },
];
