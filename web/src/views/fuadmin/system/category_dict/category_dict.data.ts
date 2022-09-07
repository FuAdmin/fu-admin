/**
 * -*- coding: utf-8 -*-
 * time: 2022/4/8 01:12
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { useI18n } from '/@/hooks/web/useI18n';
const { t } = useI18n();

export const columns: BasicColumn[] = [
  {
    title: t('common.category.showValueText'),
    dataIndex: 'label',
    width: 160,
    align: 'left',
  },
  {
    title: t('common.category.actualValueText'),
    dataIndex: 'value',
    width: 180,
  },
  {
    title: t('common.category.codeText'),
    dataIndex: 'code',
    width: 180,
  },
  {
    title: t('common.sortText'),
    dataIndex: 'sort',
    width: 50,
  },
  {
    title: t('common.remarkText'),
    dataIndex: 'remark',
  },

  {
    title: t('common.createDateText'),
    dataIndex: 'create_datetime',
    width: 180,
  },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'label',
    label: t('common.category.showValueText'),
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'value',
    label: t('common.category.actualValueText'),
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'code',
    label: t('common.category.codeText'),
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
    field: 'parent_id',
    label: t('common.category.parentText'),
    component: 'TreeSelect',
    componentProps: {
      fieldNames: {
        label: 'label',
        key: 'id',
        value: 'id',
      },
      getPopupContainer: () => document.body,
    },
  },

  {
    field: 'label',
    label: t('common.category.showValueText'),
    component: 'Input',
    required: true,
  },
  {
    field: 'value',
    label: t('common.category.actualValueText'),
    component: 'Input',
    required: true,
  },
  {
    field: 'code',
    label: t('common.category.codeText'),
    component: 'Input',
    required: true,
  },

  {
    field: 'sort',
    label: t('common.sortText'),
    defaultValue: 1,
    component: 'InputNumber',
    required: true,
  },
  {
    label: t('common.remarkText'),
    field: 'remark',
    component: 'InputTextArea',
  },
];
