
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
export const columns: BasicColumn[] = [
    
  {
    title: 'project_id',
    dataIndex: 'project_id',
    width: '80',
    fixed: '',
    align: 'left',
    auth: ['go_view_data:project_id'],
    resizable: true,
  },

  {
    title: 'content',
    dataIndex: 'content',
    width: '80',
    fixed: '',
    align: 'left',
    auth: ['go_view_data:content'],
    resizable: true,
  },

]
export const searchFormSchema: FormSchema[] = [
        
  {
    label: 'project_id',
    field: 'project_id',
    component: 'Input',
    colProps: { span: 6 },
  },

  {
    label: 'content',
    field: 'content',
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
    label: 'project_id',
    field: 'project_id',
    colProps: {
      span: 24
    },
    componentProps: {
      type: 'text'
    },
    itemProps: {
      labelCol: {},
      wrapperCol: {}
    }
  },
  {
    component: 'InputTextArea',
    label: 'content',
    field: 'content',
    colProps: {
      span: 24
    },
    componentProps: {},
    itemProps: {
      labelCol: {},
      wrapperCol: {}
    }
  }
]