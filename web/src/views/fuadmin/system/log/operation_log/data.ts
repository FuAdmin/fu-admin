/**
 * -*- coding: utf-8 -*-
 * time: 2022/5/11 01:21
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';

export const columns: BasicColumn[] = [
  {
    title: '操作用户',
    dataIndex: 'request_username',
    width: 100,
  },
  {
    title: '请求地址',
    dataIndex: 'request_path',
    width: 200,
  },
  {
    title: '请求方式',
    dataIndex: 'request_method',
    width: 100,
  },
  {
    title: '操作说明',
    dataIndex: 'request_msg',
    width: 100,
  },
  {
    title: '请求ip地址',
    dataIndex: 'request_ip',
    width: 100,
  },
  {
    title: '请求浏览器',
    dataIndex: 'request_browser',
    width: 100,
  },
  {
    title: '响应状态码',
    dataIndex: 'response_code',
    width: 100,
  },
  {
    title: '操作系统',
    dataIndex: 'request_os',
    width: 100,
  },
  {
    title: '创建时间',
    dataIndex: 'create_datetime',
    width: 180,
  },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'request_username',
    label: '操作用户',
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
    field: 'request_username',
    label: '操作用户',
    required: false,
    component: 'Input',
  },
  {
    field: 'request_path',
    label: '请求地址',
    required: false,
    component: 'Input',
  },
  {
    field: 'request_method',
    label: '请求方式',
    required: false,
    component: 'Input',
  },
  {
    field: 'request_msg',
    label: '操作说明',
    required: false,
    component: 'Input',
  },
  {
    field: 'request_ip',
    label: '请求ip地址',
    required: false,
    component: 'Input',
  },
  {
    field: 'request_browser',
    label: '请求浏览器',
    required: false,
    component: 'Input',
  },
  {
    field: 'response_code',
    label: '响应状态码',
    required: false,
    component: 'Input',
  },
  {
    field: 'request_os',
    label: '操作系统',
    required: false,
    component: 'Input',
  },
  {
    field: 'status',
    label: '响应状态',
    required: false,
    component: 'Input',
  },
  {
    field: 'request_body',
    label: '请求参数',
    required: false,
    component: 'InputTextArea',
  },
  {
    field: 'json_result',
    label: '返回信息',
    required: false,
    component: 'InputTextArea',
  },
];
