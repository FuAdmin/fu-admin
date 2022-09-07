/**
 * -*- coding: utf-8 -*-
 * time: 2022/5/11 01:21
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { useI18n } from '/@/hooks/web/useI18n';
const { t } = useI18n();

export const columns: BasicColumn[] = [
  {
    title: t('common.log.requestNameText'),
    dataIndex: 'request_username',
    width: 100,
  },
  {
    title: t('common.log.pathText'),
    dataIndex: 'request_path',
    width: 200,
  },
  {
    title: t('common.log.methodText'),
    dataIndex: 'request_method',
    width: 100,
  },
  {
    title: t('common.log.msgText'),
    dataIndex: 'request_msg',
    width: 100,
  },
  {
    title: t('common.log.ipText'),
    dataIndex: 'request_ip',
    width: 100,
  },
  {
    title: t('common.log.browserText'),
    dataIndex: 'request_browser',
    width: 100,
  },
  {
    title: t('common.log.codeText'),
    dataIndex: 'response_code',
    width: 100,
  },
  {
    title: t('common.log.osText'),
    dataIndex: 'request_os',
    width: 100,
  },
  {
    title: t('common.createDateText'),
    dataIndex: 'create_datetime',
    width: 180,
  },
];

export const searchFormSchema: FormSchema[] = [
  {
    field: 'request_username',
    label: t('common.log.requestNameText'),
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
    label: t('common.log.requestNameText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'request_path',
    label: t('common.log.pathText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'request_method',
    label: t('common.log.methodText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'request_msg',
    label: t('common.log.msgText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'request_ip',
    label: t('common.log.ipText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'request_browser',
    label: t('common.log.browserText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'response_code',
    label: t('common.log.codeText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'request_os',
    label: t('common.log.osText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'status',
    label: t('common.log.statusText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'request_body',
    label: t('common.log.bodyText'),
    required: false,
    component: 'InputTextArea',
  },
  {
    field: 'json_result',
    label: t('common.log.jsonText'),
    required: false,
    component: 'InputTextArea',
  },
];
