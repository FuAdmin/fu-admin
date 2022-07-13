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

export const columns: BasicColumn[] = [
  {
    title: '角色名称',
    dataIndex: 'name',
    width: 200,
  },
  {
    title: '角色编码',
    dataIndex: 'code',
    width: 180,
  },
  {
    title: '角色排序',
    dataIndex: 'sort',
    width: 100,
  },
  {
    title: '角色状态',
    dataIndex: 'status',
    width: 100,
    customRender: ({ record }) => {
      const status = record.status;
      const enable = ~~status === 1;
      const color = enable ? 'success' : 'error';
      const text = enable ? '启用' : '停用';
      return h(Tag, { color: color }, () => text);
    },
  },
  {
    title: '角色备注',
    dataIndex: 'remark',
    width: 280,
  },
  {
    title: '创建时间',
    dataIndex: 'create_datetime',
    width: 180,
  },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'name',
    label: '角色名称',
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'status',
    label: '角色状态',
    component: 'Select',
    componentProps: {
      options: [
        { label: '启用', value: true },
        { label: '停用', value: false },
      ],
    },
    colProps: { span: 6 },
  },
];
const isDataRange = (data_range: number) => data_range === 4;

export const formSchema: FormSchema[] = [
  {
    field: 'id',
    label: 'id',
    component: 'Input',
    show: false,
  },
  {
    field: 'name',
    label: '角色名称',
    required: true,
    component: 'Input',
  },
  {
    field: 'code',
    label: '角色编码',
    required: true,
    component: 'Input',
  },
  {
    field: 'status',
    label: '角色状态',
    component: 'RadioButtonGroup',
    defaultValue: true,
    componentProps: {
      options: [
        { label: '启用', value: true },
        { label: '停用', value: false },
      ],
    },
  },
  {
    field: 'sort',
    label: '角色排序',
    component: 'InputNumber',
    required: true,
  },
  {
    label: '角色备注',
    field: 'remark',
    component: 'InputTextArea',
  },
  //防止在更新角色信息时漏掉menu，permission，data_range，dept
  {
    field: 'menu',
    label: '菜单权限',
    component: 'Select',
    show: false,
  },

  {
    field: 'permission',
    label: '按钮权限',
    component: 'Select',
    show: false,
  },

  {
    field: 'data_range',
    label: '数据范围',
    component: 'Select',
    show: false,
  },

  {
    field: 'dept',
    label: '选择权限',
    component: 'Select',
    show: false,
  },
];

export const formPermissionSchema: FormSchema[] = [
  {
    field: 'data_range',
    label: '数据范围',
    component: 'Select',
    componentProps: ({ formModel }) => {
      return {
        options: [
          { label: '仅本人数据权限', value: 0 },
          { label: '本部门数据权限', value: 1 },
          { label: '本部门及以下数据权限', value: 2 },
          { label: '全部数据权限', value: 3 },
          { label: '自定义数据权限', value: 4 },
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
    label: '选择权限',
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
