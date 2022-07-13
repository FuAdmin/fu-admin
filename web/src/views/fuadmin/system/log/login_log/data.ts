/**
 * -*- coding: utf-8 -*-
 * time: 2022/5/8 23:42
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';

export const columns: BasicColumn[] = [
  {
    title: '登录用户',
    dataIndex: 'username',
    width: 100,
  },
  {
    title: '登录ip',
    dataIndex: 'ip',
    width: 100,
  },
  {
    title: 'agent信息',
    dataIndex: 'agent',
    width: 150,
  },
  {
    title: '操作系统',
    dataIndex: 'os',
    width: 100,
  },
  {
    title: '国家',
    dataIndex: 'country',
    width: 100,
  },
  {
    title: '省份',
    dataIndex: 'province',
    width: 100,
  },
  {
    title: '城市',
    dataIndex: 'city',
    width: 100,
  },
  {
    title: '县区',
    dataIndex: 'district',
    width: 100,
  },
  {
    title: '运营商',
    dataIndex: 'isp',
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
    field: 'username',
    label: '登录用户',
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
    field: 'username',
    label: '登录用户',
    required: false,
    component: 'Input',
  },
  {
    field: 'ip',
    label: '登录ip',
    required: false,
    component: 'Input',
  },
  {
    field: 'agent',
    label: 'agent信息',
    required: false,
    component: 'Input',
  },
  {
    field: 'browser',
    label: '浏览器名',
    required: false,
    component: 'Input',
  },
  {
    field: 'os',
    label: '操作系统',
    required: false,
    component: 'Input',
  },
  {
    field: 'continent',
    label: '州',
    required: false,
    component: 'Input',
  },
  {
    field: 'country',
    label: '国家',
    required: false,
    component: 'Input',
  },
  {
    field: 'province',
    label: '省份',
    required: false,
    component: 'Input',
  },
  {
    field: 'city',
    label: '城市',
    required: false,
    component: 'Input',
  },
  {
    field: 'district',
    label: '县区',
    required: false,
    component: 'Input',
  },
  {
    field: 'isp',
    label: '运营商',
    required: false,
    component: 'Input',
  },
  {
    field: 'area_code',
    label: '区域代码',
    required: false,
    component: 'Input',
  },
  {
    field: 'country_english',
    label: '英文全称',
    required: false,
    component: 'Input',
  },
  {
    field: 'country_code',
    label: '简称',
    required: false,
    component: 'Input',
  },
  {
    field: 'longitude',
    label: '经度',
    required: false,
    component: 'Input',
  },
  {
    field: 'latitude',
    label: '纬度',
    required: false,
    component: 'Input',
  },
];
