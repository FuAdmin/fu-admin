
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
export const columns: BasicColumn[] = [
    
  {
    title: '描述',
    dataIndex: 'des',
    width: '80',
  },

  {
    title: '编码',
    dataIndex: 'code',
    width: '80',
  },

  {
    title: '名称',
    dataIndex: 'name',
    width: '80',
  },

]
export const searchFormSchema: FormSchema[] = [
        
  {
    label: '名称',
    field: 'name',
    component: 'Input',
    colProps: { span: 6 },
  },

  {
    label: '编码',
    field: 'code',
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
    label: '名称',
    colProps: {
      span: 24
    },
    field: 'name',
  },

  {
    component: 'InputNumber',
    label: '编码',
    colProps: {
      span: 24
    },
    field: 'code',
  },

  {
    component: 'InputTextArea',
    label: '描述',
    colProps: {
      span: 24
    },
    field: 'des',
  },

]
