
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
export const columns: BasicColumn[] = [
    
  {
    title: '倒计时输入',
    dataIndex: '_input_count_down_1',
    width: '80',
  },
  
  {
    title: '密码强度',
    dataIndex: '_strength_meter_2',
    width: '80',
  },
  
]
export const searchFormSchema: FormSchema[] = [
        
  {
    label: '倒计时输入',
    field: '_input_count_down_1',
    component: 'Input',
    colProps: { span: 6 },
  },
  
  {
    label: '密码强度',
    field: '_strength_meter_2',
    component: 'Input',
    colProps: { span: 6 },
  },
  
  {
    label: '图标选择器',
    field: '_icon_picker_3',
    component: 'Input',
    colProps: { span: 6 },
  },
  
  {
    label: '自动完成',
    field: '_auto_complete_4',
    component: 'Input',
    colProps: { span: 6 },
  },
]
export const formSchema: FormSchema[] = [ 
            
  {
    component: 'InputCountDown',
    label: '倒计时输入',
    icon: 'line-md:iconify2',
    colProps:{
        span: 24
    },
    field: '_input_count_down_1',
  },
  
  {
    component: 'StrengthMeter',
    label: '密码强度',
    icon: 'wpf:password1',
    colProps:{
        span: 24
    },
    field: '_strength_meter_2',
  },
  
  {
    component: 'IconPicker',
    label: '图标选择器',
    icon: 'line-md:iconify2',
    colProps:{
        span: 24
    },
    field: '_icon_picker_3',
  },
  
  {
    component: 'AutoComplete',
    label: '自动完成',
    icon: 'wpf:password1',
    colProps:{
        span: 24
    },
    field: '_auto_complete_4',
  },
  
]
