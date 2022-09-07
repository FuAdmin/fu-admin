/**
 * -*- coding: utf-8 -*-
 * time: 2022/5/7 23:37
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { useI18n } from '/@/hooks/web/useI18n';
const { t } = useI18n();

export const columns: BasicColumn[] = [
  {
    title: t('common.log.taskIdText'),
    dataIndex: 'task_id',
    width: 100,
  },
  {
    title: t('common.log.taskText'),
    dataIndex: 'task_name',
    width: 100,
  },
  {
    title: t('common.log.nameText'),
    dataIndex: 'periodic_task_name',
    width: 100,
  },
  {
    title: t('common.statusText'),
    dataIndex: 'status',
    width: 100,
  },
  {
    title: t('common.log.resultText'),
    dataIndex: 'result',
    width: 150,
  },
  {
    title: t('common.createDateText'),
    dataIndex: 'date_created',
    width: 100,
  },
  {
    title: t('common.log.dateDoneText'),
    dataIndex: 'date_done',
    width: 100,
  },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'periodic_task_name',
    label: t('common.log.nameText'),
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
    label: t('common.log.taskIdText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'task_name',
    label: t('common.log.taskText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'periodic_task_name',
    label: t('common.log.nameText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'status',
    label: t('common.statusText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'result',
    label: t('common.log.resultText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'date_created',
    label: t('common.createDateText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'date_done',
    label: t('common.log.dateDoneText'),
    required: false,
    component: 'Input',
  },
];
