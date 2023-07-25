
import { BasicColumn } from '/@/components/Table';
import { FormSchema } from '/@/components/Table';
export const columns: BasicColumn[] = [
    
  {
    title: '输入框',
    dataIndex: 'input_1',
    width: '80',
  },

  {
    title: '数字输入框',
    dataIndex: 'input_number_2',
    width: '80',
  },

  {
    title: '下拉选择',
    dataIndex: 'select_1',
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
    label: '数字输入框',
    field: 'input_number_2',
    component: 'Input',
    colProps: { span: 6 },
  },

  {
    label: '下拉选择',
    field: 'select_1',
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
    },
    itemProps: {
      labelCol: {},
      wrapperCol: {},
      required: true,
      message: '给对方发的'
    },
    rules: [
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      }
    ]
  },
  {
    component: 'InputNumber',
    label: '数字输入框',
    field: 'input_number_2',
    colProps: {
      span: 24
    },
    componentProps: {
      style: 'width:100%'
    },
    itemProps: {
      labelCol: {},
      wrapperCol: {
        span: 24
      }
    }
  },
  {
    component: 'Select',
    label: '下拉选择',
    field: 'select_1',
    colProps: {
      span: 24
    },
    componentProps: {
      options: [
        {
          label: '选项1',
          value: '1'
        },
        {
          label: '选项2',
          value: '2'
        }
      ],
      allowClear: false
    },
    itemProps: {
      labelCol: {},
      wrapperCol: {
        span: 24
      },
      required: false,
      message: '哥哥发'
    },
    rules: [
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      },
      {
        pattern: '',
        message: ''
      }
    ]
  }
]