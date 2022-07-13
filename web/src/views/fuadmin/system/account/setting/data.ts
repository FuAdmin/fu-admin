/**
 * -*- coding: utf-8 -*-
 * time: 2022/5/30 23:32
 * author: 臧成龙
 * QQ: 939589097
 */
import { FormSchema } from '/@/components/Form';
import { rules } from '/@/utils/helper/validator';

export interface ListItem {
  key: string;
  title: string;
  description: string;
  extra?: string;
  avatar?: string;
  color?: string;
}

// tab的list
export const settingList = [
  {
    key: '1',
    name: '基本设置',
    component: 'BaseSetting',
  },
  {
    key: '2',
    name: '安全设置',
    component: 'SecureSetting',
  },
  // {
  //   key: '3',
  //   name: '账号绑定',
  //   component: 'AccountBind',
  // },
  // {
  //   key: '4',
  //   name: '新消息通知',
  //   component: 'MsgNotify',
  // },
];

// 基础设置 form
export const baseSetschemas: FormSchema[] = [
  {
    field: 'id',
    label: 'id',
    component: 'Input',
    show: false,
  },
  {
    field: 'username',
    label: '账号',
    component: 'Input',
    show: true,
    colProps: { span: 18 },
    dynamicDisabled: () => {
      return true;
    },
  },
  {
    field: 'name',
    component: 'Input',
    label: '姓名',
    colProps: { span: 18 },
  },
  {
    field: 'email',
    component: 'Input',
    label: '邮箱',
    colProps: { span: 18 },
    rules: rules.rule('email', false),
  },
  {
    field: 'mobile',
    component: 'Input',
    label: '电话',
    colProps: { span: 18 },
    rules: rules.rule('phone', false),
  },
  {
    field: 'remark',
    component: 'InputTextArea',
    label: '简介',
    colProps: { span: 18 },
  },
  {
    field: 'avatar',
    label: '用户头像',
    component: 'Input',
    ifShow: false,
  },
];

// 安全设置 list
export const secureSetschemas: FormSchema[] = [
  // {
  //   field: 'old_password',
  //   label: '当前密码',
  //   component: 'Input',
  //   show: true,
  // },
  {
    field: 'password',
    label: '输入新密码',
    component: 'InputPassword',
    show: true,
    rules: [
      {
        required: true,
        message: '请输入新密码',
      },
    ],
    colProps: { span: 18 },
  },
  {
    field: 'verify_password',
    label: '确认新密码',
    component: 'InputPassword',
    show: true,
    colProps: { span: 18 },
    dynamicRules: ({ values }) => rules.confirmPassword(values, true),
  },
];

// 账号绑定 list
export const accountBindList: ListItem[] = [
  {
    key: '1',
    title: '绑定淘宝',
    description: '当前未绑定淘宝账号',
    extra: '绑定',
    avatar: 'ri:taobao-fill',
    color: '#ff4000',
  },
  {
    key: '2',
    title: '绑定支付宝',
    description: '当前未绑定支付宝账号',
    extra: '绑定',
    avatar: 'fa-brands:alipay',
    color: '#2eabff',
  },
  {
    key: '3',
    title: '绑定钉钉',
    description: '当前未绑定钉钉账号',
    extra: '绑定',
    avatar: 'ri:dingding-fill',
    color: '#2eabff',
  },
];

// 新消息通知 list
export const msgNotifyList: ListItem[] = [
  {
    key: '1',
    title: '账户密码',
    description: '其他用户的消息将以站内信的形式通知',
  },
  {
    key: '2',
    title: '系统消息',
    description: '系统消息将以站内信的形式通知',
  },
  {
    key: '3',
    title: '待办任务',
    description: '待办任务将以站内信的形式通知',
  },
];
