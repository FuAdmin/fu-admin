/**
 * -*- coding: utf-8 -*-
 * time: 2022/5/11 22:12
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';

import { useI18n } from '/@/hooks/web/useI18n';
const { t } = useI18n();

export const columns: BasicColumn[] = [
  {
    title: t('common.column.nameText'),
    dataIndex: 'name',
    width: 50,
  },
  {
    title: t('common.column.codeText'),
    dataIndex: 'code',
    width: 70,
  },
  {
    title: t('common.createDateText'),
    dataIndex: 'create_datetime',
    width: 120,
    ifShow: false,
  },
  {
    title: t('common.remarkText'),
    dataIndex: 'remark',
    ifShow: false,
  },
];

export const columnsQuick: BasicColumn[] = [
  {
    title: t('common.column.nameText'),
    dataIndex: 'name',
    width: 100,
  },
  {
    title: t('common.column.codeText'),
    dataIndex: 'code',
    width: 100,
  },
];

// @ts-ignore
// @ts-ignore
export const formSchema: FormSchema[] = [
  {
    field: 'id',
    label: 'id',
    component: 'Input',
    show: false,
  },
  {
    field: 'name',
    label: t('common.column.nameText'),
    component: 'Input',
    required: true,
  },
  {
    field: 'code',
    label: t('common.column.codeText'),
    required: true,
    component: 'Input',
    show: true,
  },
  {
    field: 'sort',
    label: t('common.sortText'),
    component: 'InputNumber',
    defaultValue: 1,
    required: true,
  },
  {
    label: t('common.remarkText'),
    field: 'remark',
    component: 'InputTextArea',
  },
];
