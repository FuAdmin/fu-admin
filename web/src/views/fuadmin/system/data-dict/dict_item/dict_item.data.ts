/**
 * -*- coding: utf-8 -*-
 * time: 2022/4/28 23:34
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { h } from 'vue';
import { Tag } from 'ant-design-vue';
import { useI18n } from '/@/hooks/web/useI18n';
import { SvgIcon } from "/@/components/Icon";
const { t } = useI18n();

export const columns: BasicColumn[] = [
  {
    title: t('common.menu.iconText'),
    dataIndex: 'icon',
    width: 100,
    customRender: ({ record }) => {
      return h(SvgIcon, { name: record.icon });
    },
  },
  {
    title: t('common.dict.showValueText'),
    dataIndex: 'label',
    width: 50,
  },
  {
    title: t('common.dict.actualValueText'),
    dataIndex: 'value',
    width: 70,
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
    width: 120,
    ifShow: false,
  },
  {
    title: t('common.remarkText'),
    dataIndex: 'remark',
    ifShow: false,
  },
];

// @ts-ignore
// @ts-ignore
export const formSchema: FormSchema[] = [
  {
    field: 'icon',
    label: t('common.menu.iconText'),
    component: 'IconPicker',
    required: false,
    componentProps: {
      mode: 'svg',
    },
  },
  {
    field: 'id',
    label: 'id',
    component: 'Input',
    show: false,
  },
  {
    field: 'label',
    label: t('common.dict.showValueText'),
    component: 'Input',
    required: true,
  },
  {
    field: 'value',
    label: t('common.dict.actualValueText'),
    required: true,
    component: 'Input',
    show: true,
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
