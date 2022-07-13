/**
 * -*- coding: utf-8 -*-
 * time: 2022/5/11 22:12
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { h } from 'vue';
import { Tag } from 'ant-design-vue';

const methodOptions = [
  { label: 'GET', value: 0 },
  { label: 'POST', value: 1 },
  { label: 'PUT', value: 2 },
  { label: 'DELETE', value: 3 },
];

export const columns: BasicColumn[] = [
  {
    title: '按钮名称',
    dataIndex: 'name',
    width: 50,
  },
  {
    title: '按钮编码',
    dataIndex: 'code',
    width: 70,
  },
  {
    title: '请求方式',
    dataIndex: 'method',
    width: 50,
    customRender: ({ record }) => {
      const method = record.method;
      let color = '';
      let text = '';
      switch (method) {
        case 0:
          color = 'processing';
          text = 'GET';
          break;
        case 1:
          color = 'success';
          text = 'POST';
          break;
        case 2:
          color = 'warning';
          text = 'PUT';
          break;
        case 3:
          color = 'error';
          text = 'DELETE';
          break;
      }
      return h(Tag, { color: color }, () => text);
    },
  },
  {
    title: '按钮接口',
    dataIndex: 'api',
    width: 100,
  },
  {
    title: '创建时间',
    dataIndex: 'create_datetime',
    width: 120,
    ifShow: false,
  },
  {
    title: '按钮备注',
    dataIndex: 'remark',
    ifShow: false,
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
    label: '按钮名称',
    component: 'Input',
    required: true,
  },
  {
    field: 'code',
    label: '按钮编码',
    required: true,
    component: 'Input',
    show: true,
  },

  {
    field: 'method',
    label: '请求方式',
    component: 'Select',
    componentProps: {
      options: methodOptions,
    },
    required: true,
  },

  {
    field: 'api',
    label: '按钮接口',
    required: true,
    component: 'Input',
  },

  // {
  //   field: 'status',
  //   label: '按钮状态',
  //   component: 'RadioButtonGroup',
  //   defaultValue: true,
  //   componentProps: {
  //     options: [
  //       { label: '启用', value: true },
  //       { label: '停用', value: false },
  //     ],
  //   },
  // },
  {
    field: 'sort',
    label: '按钮排序',
    component: 'InputNumber',
    defaultValue: 1,
    required: true,
  },
  {
    label: '按钮备注',
    field: 'remark',
    component: 'InputTextArea',
  },
];
