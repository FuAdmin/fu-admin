/**
 * -*- coding: utf-8 -*-
 * time: 2022/5/15 23:59
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { h } from 'vue';
import { Tag } from 'ant-design-vue';
import Icon  from '/@/components/Icon/Icon.vue';
import { useI18n } from '/@/hooks/web/useI18n';
const { t } = useI18n();

export const columns: BasicColumn[] = [
  {
    title: t('common.menu.titleText'),
    dataIndex: 'title',
    width: 200,
    align: 'left',
  },
  {
    title: t('common.menu.iconText'),
    dataIndex: 'icon',
    width: 100,
    customRender: ({ record }) => {
      return h(Icon, { icon: record.icon });
    },
  },
  {
    title: t('common.menu.pathText'),
    dataIndex: 'path',
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
    title: t('common.createDateText'),
    dataIndex: 'create_datetime',
    width: 180,
  },
];

const isDir = (type: number) => type === 0;
const isMenu = (type: number) => type === 1;

export const searchFormSchema: FormSchema[] = [
  {
    field: 'title',
    label: t('common.menu.titleText'),
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
    field: 'type',
    label: t('common.menu.typeText'),
    component: 'RadioButtonGroup',
    defaultValue: 0,
    componentProps: {
      options: [
        { label: t('common.menu.directoryText'), value: 0 },
        { label: t('common.menu.menuText'), value: 1 },
      ],
    },
    colProps: { lg: 24, md: 24 },
  },
  {
    field: 'title',
    label: t('common.menu.titleText'),
    component: 'Input',
    required: true,
  },

  {
    field: 'parent_id',
    label: t('common.menu.parentText'),
    component: 'TreeSelect',
    componentProps: {
      fieldNames: {
        label: 'title',
        key: 'id',
        value: 'id',
      },
      getPopupContainer: () => document.body,
    },
  },

  {
    field: 'sort',
    label: t('common.sortText'),
    component: 'InputNumber',
    defaultValue: 1,
  },
  {
    field: 'icon',
    label: t('common.menu.iconText'),
    component: 'IconPicker',
    required: false,
  },

  {
    field: 'path',
    label: t('common.menu.pathText'),
    component: 'Input',
    // helpMessage: '请用/开头',
    required: true,
  },

  {
    field: 'redirect',
    label: t('common.menu.redirectText'),
    component: 'Input',
    required: false,
    ifShow: ({ values }) => isDir(values.type),
  },

  {
    field: 'component',
    label: t('common.menu.componentText'),
    component: 'Input',
    ifShow: ({ values }) => isMenu(values.type),
  },
  {
    field: 'name',
    label: t('common.menu.nameText'),
    component: 'Input',
    ifShow: ({ values }) => isMenu(values.type),
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
    field: 'is_ext',
    label: t('common.menu.isExtText'),
    component: 'RadioButtonGroup',
    defaultValue: false,
    componentProps: {
      options: [
        { label: t('common.yesText'), value: true },
        { label: t('common.noText'), value: false },
      ],
    },
    ifShow: ({ values }) => isMenu(values.type),
  },

  {
    field: 'keepalive',
    label: t('common.menu.keepaliveText'),
    component: 'RadioButtonGroup',
    defaultValue: false,
    componentProps: {
      options: [
        { label: t('common.yesText'), value: true },
        { label: t('common.noText'), value: false },
      ],
    },
    ifShow: ({ values }) => isMenu(values.type),
  },

  {
    field: 'hide_menu',
    label: t('common.menu.hideMenuText'),
    component: 'RadioButtonGroup',
    defaultValue: false,
    componentProps: {
      options: [
        { label: t('common.yesText'), value: true },
        { label: t('common.noText'), value: false },
      ],
    },
  },
];
