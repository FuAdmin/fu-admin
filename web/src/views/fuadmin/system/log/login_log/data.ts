/**
 * -*- coding: utf-8 -*-
 * time: 2022/5/8 23:42
 * author: 臧成龙
 * QQ: 939589097
 */
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
import { useI18n } from '/@/hooks/web/useI18n';
const { t } = useI18n();

export const columns: BasicColumn[] = [
  {
    title: t('common.log.loginUserText'),
    dataIndex: 'username',
    width: 100,
  },
  {
    title: t('common.log.ipText'),
    dataIndex: 'ip',
    width: 100,
  },
  {
    title: t('common.log.agentText'),
    dataIndex: 'agent',
    width: 150,
  },
  {
    title: t('common.log.osText'),
    dataIndex: 'os',
    width: 100,
  },
  {
    title: t('common.log.countryText'),
    dataIndex: 'country',
    width: 100,
  },
  {
    title: t('common.log.provinceText'),
    dataIndex: 'province',
    width: 100,
  },
  {
    title: t('common.log.cityText'),
    dataIndex: 'city',
    width: 100,
  },
  {
    title: t('common.log.districtText'),
    dataIndex: 'district',
    width: 100,
  },
  {
    title: t('common.log.ispText'),
    dataIndex: 'isp',
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
    field: 'username',
    label: t('common.log.loginUserText'),
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
    label: t('common.log.loginUserText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'ip',
    label: t('common.log.ipText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'agent',
    label: t('common.log.agentText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'browser',
    label: t('common.log.browserText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'os',
    label: t('common.log.osText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'continent',
    label: t('common.log.continentText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'country',
    label: t('common.log.countryText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'province',
    label: t('common.log.provinceText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'city',
    label: t('common.log.cityText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'district',
    label: t('common.log.districtText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'isp',
    label: t('common.log.ispText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'area_code',
    label: t('common.log.areaCodeText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'country_english',
    label: t('common.log.countryEnglishText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'country_code',
    label: t('common.log.countryCodeText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'longitude',
    label: t('common.log.longitudeText'),
    required: false,
    component: 'Input',
  },
  {
    field: 'latitude',
    label: t('common.log.latitudeCodeText'),
    required: false,
    component: 'Input',
  },
];
