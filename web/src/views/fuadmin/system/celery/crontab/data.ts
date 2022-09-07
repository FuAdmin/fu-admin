/**
 * -*- coding: utf-8 -*-
 * time: 2022/4/12 22:53
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { getCrontabData } from '/@/views/fuadmin/system/celery/util';
import { useI18n } from '/@/hooks/web/useI18n';
import { computed } from 'vue';
import { useLocaleStoreWithOut } from '/@/store/modules/locale';
const { t } = useI18n();
const localeStore = useLocaleStoreWithOut();

const getLocale = computed(() => localeStore.getLocale).value;

export const columns: BasicColumn[] = [
  {
    title: '',
    dataIndex: 'code',
    width: 300,
    customRender: ({ record }) => {
      if (getLocale === 'zh_CN') {
        return getCrontabData(record);
      } else {
        return `${record.month_of_year} ${record.day_of_month} ${record.day_of_week} ${record.hour} ${record.minute} `;
      }
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
    label: t('common.task.minuteText'),
    defaultValue: '*',
    required: true,
    component: 'Input',
  },
  {
    field: 'hour',
    label: t('common.task.hourText'),
    defaultValue: '*',
    required: true,
    component: 'Input',
  },
  {
    field: 'day_of_week',
    label: t('common.task.dayOfWeekText'),
    defaultValue: '*',
    required: true,
    component: 'Input',
  },
  {
    field: 'day_of_month',
    label: t('common.task.dayOfMonthText'),
    defaultValue: '*',
    required: true,
    component: 'Input',
  },
  {
    field: 'month_of_year',
    label: t('common.task.monthOfYearText'),
    defaultValue: '*',
    required: true,
    component: 'Input',
  },
];
