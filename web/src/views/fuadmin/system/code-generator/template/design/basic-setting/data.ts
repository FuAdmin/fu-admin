import { FormSchema } from '/@/components/Form';

/**
 * -*- coding: utf-8 -*-
 * time: 6/30/2023 3:36 PM
 * file: data.ts
 * author: 臧成龙
 * QQ: 939589097
 */
export const schemas: FormSchema[] = [
  {
    field: 'template_name',
    component: 'Input',
    label: '模板名称',
    componentProps: {
      // placeholder: '自定义placeholder',
    },
  },
  {
    field: 'template_code',
    component: 'Input',
    label: '模板编码',
    componentProps: {
      // placeholder: '自定义placeholder',
    },
  },

  {
    field: 'template_des',
    component: 'Input',
    label: '模板说明',
    componentProps: {
      // placeholder: '自定义placeholder',
    },
  },
];
