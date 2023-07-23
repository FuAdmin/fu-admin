
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
export const columns: BasicColumn[] = [
    
  {
    title: '输入框',
    dataIndex: 'input_1',
    width: '80',
  },

  {
    title: '文本域',
    dataIndex: 'input_text_area_2',
    width: '80',
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

];
export const formSchema: FormSchema[] = [
  {
    field: 'id',
    label: 'id',
    component: 'Input',
    show: false,
  },

  {
    component: 'Input',
    label: '输入框',
    colProps: {
      span: 24
    },
    field: 'input_1',
  },

  {
    component: 'InputTextArea',
    label: '文本域',
    colProps: {
      span: 24
    },
    field: 'input_text_area_2',
  },

]
