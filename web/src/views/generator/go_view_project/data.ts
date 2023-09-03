
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
export const columns: BasicColumn[] = [
    
  {
    title: 'project_name',
    dataIndex: 'project_name',
    width: '80',
    fixed: '',
    align: 'left',
    auth: ['go_view_project:project_name'],
    resizable: true,
  },

  {
    title: 'state',
    dataIndex: 'state',
    width: '80',
    fixed: '',
    align: 'left',
    auth: ['go_view_project:state'],
    resizable: true,
  },

  {
    title: 'index_image',
    dataIndex: 'index_image',
    width: '80',
    fixed: '',
    align: 'left',
    auth: ['go_view_project:index_image'],
    resizable: true,
  },

]
export const searchFormSchema: FormSchema[] = [
        
  {
    label: 'project_name',
    field: 'project_name',
    component: 'Input',
    colProps: { span: 6 },
  },

  {
    label: 'state',
    field: 'state',
    component: 'Input',
    colProps: { span: 6 },
  },

  {
    label: 'index_image',
    field: 'index_image',
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
    label: 'project_name',
    field: 'project_name',
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
    component: 'Input',
    label: 'state',
    field: 'state',
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
    component: 'Input',
    label: 'index_image',
    field: 'index_image',
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
  }
]