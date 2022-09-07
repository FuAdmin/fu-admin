/**
 * -*- coding: utf-8 -*-
 * time: 2022/5/4 01:13
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { useI18n } from '/@/hooks/web/useI18n';
const { t } = useI18n();

export const columns: BasicColumn[] = [
  {
    title: t('common.file.fileNameText'),
    dataIndex: 'name',
    width: 100,
  },
  {
    title: t('common.file.saveNameText'),
    dataIndex: 'save_name',
    width: 100,
  },
  {
    title: t('common.file.sizeText'),
    dataIndex: 'size',
    width: 100,
  },
  {
    title: t('common.file.urlText'),
    dataIndex: 'url',
    width: 200,
  },
  {
    title: t('common.createDateText'),
    dataIndex: 'create_datetime',
    width: 100,
  },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'name',
    label: t('common.file.fileNameText'),
    component: 'Input',
    colProps: { span: 8 },
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
    field: 'name',
    label: t('common.file.fileNameText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'size',
    label: t('common.file.sizeText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'save_name',
    label: t('common.file.saveNameText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'url',
    label: t('common.file.urlText'),
    required: false,
    component: 'Input',
  },
];
