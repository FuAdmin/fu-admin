/**
 * -*- coding: utf-8 -*-
 * time: 2022/5/26 22:18
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
    title: t('common.role.nameText'),
    dataIndex: 'name',
    width: 200,
  },
  {
    title: t('common.role.codeText'),
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
    title: t('common.remarkText'),
    dataIndex: 'remark',
    width: 280,
  },
  {
    title: t('common.createDateText'),
    dataIndex: 'create_datetime',
    width: 180,
  },

  {
    dataIndex: 'menu',
    title: t('common.role.menuPermissionText'),
    ifShow: false,
  },

  {
    dataIndex: 'permission',
    title: t('common.role.buttonPermissionText'),
    ifShow: false,
  },

  {
    dataIndex: 'column',
    title: t('common.role.columnPermissionText'),
    ifShow: false,
  },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'name',
    label: t('common.role.nameText'),
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
const isDataRange = (data_range: number) => data_range === 3;

export const formSchema: FormSchema[] = [
  {
    field: 'id',
    label: 'id',
    component: 'Input',
    show: false,
  },
  {
    field: 'name',
    label: t('common.role.nameText'),
    required: true,
    component: 'Input',
  },
  {
    field: 'code',
    label: t('common.role.codeText'),
    required: true,
    component: 'Input',
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
    required: true,
  },
  {
    label: t('common.remarkText'),
    field: 'remark',
    component: 'InputTextArea',
  },
  //防止在更新角色信息时漏掉menu，permission，data_range，dept
  {
    field: 'menu',
    label: t('common.role.menuPermissionText'),
    component: 'Select',
    show: false,
  },

  {
    field: 'permission',
    label: t('common.role.buttonPermissionText'),
    component: 'Select',
    show: false,
  },

  {
    field: 'column',
    label: t('common.role.columnPermissionText'),
    component: 'Select',
    show: false,
  },

  {
    field: 'data_range',
    label: t('common.role.dataPermissionText'),
    component: 'Select',
    show: false,
  },

  {
    field: 'dept',
    label: t('common.role.choosePermissionText'),
    component: 'Select',
    show: false,
  },
];

export const formPermissionSchema: FormSchema[] = [
  {
    field: 'data_range',
    label: t('common.role.dataPermissionText'),
    component: 'Select',
    componentProps: ({ formModel }) => {
      return {
        options: [
          { label: t('common.role.onlyOwnDataText'), value: 0 },
          { label: t('common.role.onlyDeptDataText'), value: 1 },
          { label: t('common.role.deptAndBelowDataText'), value: 2 },
          { label: t('common.role.customizeOwnDataText'), value: 3 },
          { label: t('common.role.allDataText'), value: 4 },
        ],
        onChange: () => {
          formModel.dept = [];
        },
      };
    },
    required: false,
  },

  {
    field: 'dept',
    label: t('common.role.choosePermissionText'),
    component: 'TreeSelect',
    componentProps: {
      treeCheckable: true,
      fieldNames: {
        label: 'name',
        key: 'id',
        value: 'id',
      },
      getPopupContainer: () => document.body,
    },
    ifShow: ({ values }) => isDataRange(values.data_range),
  },
  // {
  //   field: 'column_permission',
  //   label: '列权限',
  //   component: 'Select',
  //   componentProps: {
  //     fieldNames: {
  //       label: 'title',
  //       key: 'dataIndex',
  //       value: 'dataIndex',
  //     },
  //   },
  // },
];
