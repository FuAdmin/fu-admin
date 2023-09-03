
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
export const columns: BasicColumn[] = [
    
  {
    title: '输入框',
    dataIndex: 'input_1',
    width: '80',
    fixed: '',
    align: 'left',
    auth: ['test_one:input_1'],
    resizable: true,
  },

  {
    title: '文本域',
    dataIndex: 'input_text_area_2',
    width: '80',
    fixed: '',
    align: 'left',
    auth: ['test_one:input_text_area_2'],
    resizable: true,
  },

  {
    title: '数字输入框',
    dataIndex: 'input_number_3',
    width: '80',
    fixed: '',
    align: 'left',
    auth: ['test_one:input_number_3'],
    resizable: true,
  },

]
export const searchFormSchema: FormSchema[] = [
        
  {
    label: '输入框',
    field: 'input_1',
    component: 'Input',
    colProps: { span: 6 },
  },

  {
    label: '文本域',
    field: 'input_text_area_2',
    component: 'Input',
    colProps: { span: 6 },
  },

  {
    label: '数字输入框',
    field: 'input_number_3',
    component: 'Input',
    colProps: { span: 6 },
  },

];
export const formSchema: FormSchema[] = [
  {
    field: 'id',
    label: 'id',
    component: 'Input',
    show: false
  },
  {
    component: 'Input',
    label: '输入框',
    field: 'input_1',
    colProps: {
      span: 24
    },
    componentProps: {
      type: 'text'
    }
  },
  {
    component: 'InputTextArea',
    label: '文本域',
    field: 'input_text_area_2',
    colProps: {
      span: 24
    },
    componentProps: {}
  },
  {
    component: 'InputNumber',
    label: '数字输入框',
    field: 'input_number_3',
    colProps: {
      span: 24
    },
    componentProps: {
      style: 'width:200px'
    }
  }
]