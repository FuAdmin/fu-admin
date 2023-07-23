
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
export const columns: BasicColumn[] = [
    
  {
    title: '名称',
    dataIndex: 'name',
    width: '80',
  },

  {
    title: '代码',
    dataIndex: 'code',
    width: '80',
  },

  {
    title: '排序',
    dataIndex: 'input_number_6',
    width: '80',
  },

  {
    title: '图标',
    dataIndex: 'icon',
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
    label: '代码',
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
    component: 'Input',
    label: '代码',
    colProps: {
      span: 24
    },
    field: 'code',
  },

  {
    component: 'InputNumber',
    label: '排序',
    colProps: {
      span: 24
    },
    field: 'sequence',
  },

  {
    component: 'IconPicker',
    label: '图标',
    colProps: {
      span: 24
    },
    field: 'icon',
  },

]
