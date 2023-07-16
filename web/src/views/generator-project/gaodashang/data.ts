import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
export const columns: BasicColumn[] = [
  {
    title: '图标选择器',
    dataIndex: '_icon_picker_2',
    width: '80',
  },

  {
    title: '密码强度',
    dataIndex: '_strength_meter_3',
    width: '80',
  },

  {
    title: '自动完成',
    dataIndex: '_auto_complete_4',
    width: '80',
  },

  {
    title: '分割线',
    dataIndex: '_divider_5',
    width: '80',
  },

  {
    title: '文本域',
    dataIndex: '_input_text_area_2',
    width: '80',
  },
];
export const searchFormSchema: FormSchema[] = [
  {
    label: '倒计时输入',
    field: '_input_count_down_1',
    component: 'Input',
    colProps: { span: 6 },
  },

  {
    label: '图标选择器',
    field: '_icon_picker_2',
    component: 'Input',
    colProps: { span: 6 },
  },

  {
    label: '密码强度',
    field: '_strength_meter_3',
    component: 'Input',
    colProps: { span: 6 },
  },
];
export const formSchema: FormSchema[] = [
  {
    component: 'InputCountDown',
    label: '倒计时输入',
    colProps: {
      span: 12,
    },
    field: '_input_count_down_1',
  },

  {
    component: 'IconPicker',
    label: '图标选择器',
    colProps: {
      span: 12,
    },
    field: '_icon_picker_2',
  },

  {
    component: 'StrengthMeter',
    label: '密码强度',
    colProps: {
      span: 12,
    },
    field: '_strength_meter_3',
  },

  {
    component: 'AutoComplete',
    label: '自动完成',
    colProps: {
      span: 12,
    },
    field: '_auto_complete_4',
  },

  {
    component: 'Divider',
    label: '分割线',
    colProps: {
      span: 24,
    },
    field: '_divider_5',
  },

  {
    component: 'InputTextArea',
    label: '文本域',
    colProps: {
      span: 24,
    },
    field: '_input_text_area_2',
  },
];
