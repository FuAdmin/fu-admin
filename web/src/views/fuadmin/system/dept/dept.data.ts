/**
 * -*- coding: utf-8 -*-
 * time: 2022/5/3 22:12
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { h } from 'vue';
import { Tag } from 'ant-design-vue';
import { rules } from '/@/utils/helper/validator';
import { useI18n } from '/@/hooks/web/useI18n';
const { t } = useI18n();

export const columns: BasicColumn[] = [
  {
    title: t('common.dept.nameText'),
    dataIndex: 'name',
    width: 160,
    align: 'left',
  },
  {
    title: t('common.dept.phoneText'),
    dataIndex: 'phone',
    width: 180,
  },
  {
    title: t('common.dept.mailText'),
    dataIndex: 'email',
    width: 180,
  },
  {
    title: t('common.sortText'),
    dataIndex: 'sort',
    width: 50,
  },
  {
    title: t('common.statusText'),
    dataIndex: 'status',
    width: 80,
    customRender: ({ record }) => {
      const status = record.status;
      const enable = ~~status === 1;
      const color = enable ? 'success' : 'error';
      const text = enable ? t('common.enableText') : t('common.disableText');
      return h(Tag, { color: color }, () => text);
    },
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
    field: 'name',
    label: t('common.dept.nameText'),
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'status',
    label: t('common.statusText'),
    component: 'Select',
    componentProps: {
      options: [
        { label: t('common.enableText'), value: true },
        { label: t('common.disableText'), value: false },
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
    field: 'parent_id',
    label: t('common.dept.parentText'),
    component: 'TreeSelect',
    componentProps: {
      fieldNames: {
        label: 'name',
        key: 'id',
        value: 'id',
      },
      getPopupContainer: () => document.body,
    },
  },

  {
    field: 'name',
    label: t('common.dept.nameText'),
    component: 'Input',
    required: true,
  },
  {
    field: 'phone',
    label: t('common.dept.phoneText'),
    component: 'Input',
    rules: rules.rule('phone', false),
  },
  {
    field: 'email',
    label: t('common.dept.mailText'),
    component: 'Input',
    rules: rules.rule('email', false),
  },

  {
    field: 'sort',
    label: t('common.sortText'),
    component: 'InputNumber',
    required: true,
  },
  {
    field: 'status',
    label: t('common.statusText'),
    component: 'RadioButtonGroup',
    defaultValue: true,
    componentProps: {
      options: [
        { label: t('common.enableText'), value: true },
        { label: t('common.disableText'), value: false },
      ],
    },
    required: true,
  },
  {
    label: t('common.remarkText'),
    field: 'remark',
    component: 'InputTextArea',
  },
];
