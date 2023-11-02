/**
 * -*- coding: utf-8 -*-
 * time: 2022/4/01 22:54
 * author: 臧成龙
 * QQ: 939589097
 */

import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { h } from 'vue';
import { Tag, Image } from 'ant-design-vue';
import { rules } from '/@/utils/helper/validator';
import { getAllList } from '/@/views/fuadmin/system/role/role.api';
import { getAllList as getPostAllList } from '/@/views/fuadmin/system/post/post.api';
import { useI18n } from '/@/hooks/web/useI18n';
const { t } = useI18n();

export const columns: BasicColumn[] = [
  {
    title: t('common.account.accountText'),
    dataIndex: 'username',
    width: 110,
  },
  {
    title: t('common.account.userNameText'),
    dataIndex: 'name',
    width: 110,
  },
  {
    title: t('common.account.avatarText'),
    dataIndex: 'avatar',
    width: 110,
    customRender: ({ record }) => {
      const avatar = record.avatar;
      return h(Image, { src: avatar, width: 40 });
    },
  },
  {
    title: t('common.account.emailText'),
    dataIndex: 'email',
    width: 120,
  },
  {
    title: t('common.account.mobileText'),
    dataIndex: 'mobile',
    width: 120,
  },
  {
    title: t('common.account.genderText'),
    dataIndex: 'gender',
    width: 110,
    customRender: ({ record }) => {
      const gender = record.gender;
      // const enable = ~~status === 1;
      const color = gender ? 'cyan' : 'purple';
      const text = gender ? t('common.account.maleText') : t('common.account.femaleText');
      return h(Tag, { color: color }, () => text);
    },
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
    label: t('common.account.userNameText'),
    component: 'Input',
    colProps: { span: 6 },
  },
  {
    field: 'mobile',
    label: t('common.account.mobileText'),
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

export const accountFormSchema: FormSchema[] = [
  {
    field: 'id',
    label: 'id',
    component: 'Input',
    show: false,
  },
  {
    field: 'password',
    label: 'password',
    component: 'Input',
    show: false,
  },
  {
    field: 'username',
    label: t('common.account.accountText'),
    component: 'Input',
    required: true,
  },
  {
    field: 'name',
    label: t('common.account.userNameText'),
    component: 'Input',
    required: true,
  },

  {
    field: 'mobile',
    label: t('common.account.mobileText'),
    component: 'Input',
    rules: rules.rule('phone', false),
  },
  {
    field: 'email',
    label: t('common.account.emailText'),
    component: 'Input',
    rules: rules.rule('email', false),
  },
  {
    label: t('common.account.userRoleText'),
    field: 'role',
    component: 'ApiSelect',
    componentProps: {
      api: getAllList,
      labelField: 'name',
      valueField: 'id',
      mode: 'multiple',
    },
    itemProps: { validateTrigger: 'blur' },
  },
  {
    label: t('common.account.userPostText'),
    field: 'post',
    component: 'ApiSelect',
    componentProps: {
      api: getPostAllList,
      labelField: 'name',
      valueField: 'id',
      mode: 'multiple',
    },
    itemProps: { validateTrigger: 'blur' },
  },
  {
    field: 'dept',
    label: t('common.account.userDeptText'),
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
    field: 'home_path',
    label: t('common.account.homePath'),
    component: 'DictSelect',
    componentProps: {
      dictCode: 'home_path',
    },
  },
  {
    field: 'gender',
    label: t('common.account.genderText'),
    component: 'RadioButtonGroup',
    defaultValue: 1,
    componentProps: {
      options: [
        { label: t('common.account.maleText'), value: 1 },
        { label: t('common.account.femaleText'), value: 0 },
      ],
    },
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
    field: 'avatar',
    label: t('common.account.avatarText'),
    component: 'Input',
    slot: 'avatar',
  },
];
