/**
 * -*- coding: utf-8 -*-
 * time: 2022/5/26 23:54
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { h } from 'vue';
import { Tag } from 'ant-design-vue';
import { useI18n } from '/@/hooks/web/useI18n';
const { t } = useI18n();

export const columns: BasicColumn[] = [
  {
    title: t('common.post.nameText'),
    dataIndex: 'name',
    width: 200,
  },
  {
    title: t('common.post.codeText'),
    dataIndex: 'code',
    width: 180,
  },
  {
    title: t('common.sortText'),
    dataIndex: 'sort',
    width: 100,
  },
  {
    title: t('common.statusText'),
    dataIndex: 'status',
    width: 100,
    customRender: ({ record }) => {
      const status = record.status;
      const enable = ~~status === 1;
      const color = enable ? 'success' : 'error';
      const text = enable ? t('common.enableText') : t('common.disableText');
      return h(Tag, { color: color }, () => text);
    },
  },
  {
    title: t('common.createDateText'),
    dataIndex: 'create_datetime',
    width: 180,
  },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'name',
    label: t('common.post.nameText'),
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'status',
    label: t('common.statusText'),
    component: 'Select',
    componentProps: {
      options: [
        { label: t('common.enableText'), value: 1 },
        { label: t('common.disableText'), value: 0 },
      ],
    },
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
    field: 'name',
    label: t('common.post.nameText'),
    required: true,
    component: 'Input',
  },
  {
    field: 'code',
    label: t('common.post.codeText'),
    required: true,
    component: 'Input',
  },
  // {
  //   field: 'field',
  //   component: 'DictSelect',
  //   label: '字段',
  //   componentProps: {
  //     dictCode: 'status',
  //   },
  // },
  {
    field: 'status',
    label: t('common.statusText'),
    component: 'RadioButtonGroup',
    defaultValue: 1,
    componentProps: {
      options: [
        { label: t('common.enableText'), value: 1 },
        { label: t('common.disableText'), value: 0 },
      ],
    },
  },
  {
    field: 'sort',
    label: t('common.sortText'),
    component: 'InputNumber',
    required: true,
  },
];
