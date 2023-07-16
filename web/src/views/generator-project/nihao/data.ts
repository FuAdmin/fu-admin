
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
export const columns: BasicColumn[] = [
    
  {
    title: '倒计时输入',
    dataIndex: '_input_count_down_1',
    width: '80',
  },
  
  {
    title: '图标选择器',
    dataIndex: '_icon_picker_2',
    width: '80',
  },
  
  {
    title: '自动完成',
    dataIndex: '_auto_complete_3',
    width: '80',
  },
  
  {
    title: '复选框',
    dataIndex: '_checkbox_4',
    width: '80',
  },
  
  {
    title: '分割线',
    dataIndex: '_divider_5',
    width: '80',
  },
  
  {
    title: '日期范围',
    dataIndex: '_range_picker_6',
    width: '80',
  },
  
  {
    title: '月份选择',
    dataIndex: '_month_picker_7',
    width: '80',
  },
  
  {
    title: '时间选择',
    dataIndex: '_time_picker_8',
    width: '80',
  },
  
  {
    title: '滑动输入条',
    dataIndex: '_slider_9',
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
    label: '图标选择器',
    field: '_icon_picker_2',
    component: 'Input',
    colProps: { span: 6 },
  },
  
  {
    label: '自动完成',
    field: '_auto_complete_3',
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
    component: 'IconPicker',
    label: '图标选择器',
    icon: 'line-md:iconify2',
    colProps:{
        span: 24
    },
    field: '_icon_picker_2',
  },
  
  {
    component: 'AutoComplete',
    label: '自动完成',
    icon: 'wpf:password1',
    colProps:{
        span: 24
    },
    field: '_auto_complete_3',
  },
  
  {
    component: 'Checkbox',
    label: '复选框',
    icon: 'ant-design:check-circle-outlined',
    colProps:{
        span: 24
    },
    field: '_checkbox_4',
  },
  
  {
    component: 'Divider',
    label: '分割线',
    icon: 'radix-icons:divider-horizontal',
    colProps:{
        span: 24
    },
    field: '_divider_5',
  },
  
  {
    component: 'RangePicker',
    label: '日期范围',
    icon: 'healthicons:i-schedule-school-date-time-outline',
    colProps:{
        span: 24
    },
    field: '_range_picker_6',
  },
  
  {
    component: 'MonthPicker',
    label: '月份选择',
    icon: 'healthicons:i-schedule-school-date-time-outline',
    colProps:{
        span: 24
    },
    field: '_month_picker_7',
  },
  
  {
    component: 'TimePicker',
    label: '时间选择',
    icon: 'healthicons:i-schedule-school-date-time',
    colProps:{
        span: 24
    },
    field: '_time_picker_8',
  },
  
  {
    component: 'Slider',
    label: '滑动输入条',
    icon: 'vaadin:slider',
    colProps:{
        span: 24
    },
    field: '_slider_9',
  },
  
]
