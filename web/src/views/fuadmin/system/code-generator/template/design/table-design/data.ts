import { BasicColumn } from '/@/components/Table';

export const searchColumns: BasicColumn[] = [
  {
    title: '列名',
    dataIndex: 'column_name',
    width: 200,
  },
  {
    title: '字段',
    dataIndex: 'field_name',
    width: 200,
  },
  {
    title: '类型',
    dataIndex: 'type',
    edit: true,
    editComponent: 'Select',
    editComponentProps: {
      options: [
        {
          label: 'none',
          value: '',
        },
        {
          label: 'left',
          value: 'left',
        },
        {
          label: 'right',
          value: 'right',
        },
      ],
    },
    width: 180,
  },
  {
    title: '是否多选',
    dataIndex: 'is_check',
    edit: true,
    editComponent: 'Checkbox',
    editValueMap: (value) => {
      return value ? '是' : '否';
    },
    width: 180,
  },
];
export const columnFieldsColumns: BasicColumn[] = [
  {
    title: '列名',
    dataIndex: 'column_name',
    width: 200,
  },
  {
    title: '字段',
    dataIndex: 'field_name',
    width: 200,
  },
  {
    title: '排序',
    dataIndex: 'sort',
    edit: true,
    editRule: true,
    editComponent: 'InputNumber',
    editComponentProps: () => {
      return {
        max: 100,
        min: 0,
      };
    },
    width: 180,
  },
  {
    title: '冻结',
    dataIndex: 'freeze',
    edit: true,
    editComponent: 'Select',
    editComponentProps: {
      options: [
        {
          label: 'none',
          value: '',
        },
        {
          label: 'left',
          value: 'left',
        },
        {
          label: 'right',
          value: 'right',
        },
      ],
    },
    width: 180,
  },
  {
    title: '对齐',
    dataIndex: 'align',
    edit: true,
    editComponent: 'Select',
    editComponentProps: {
      options: [
        {
          label: 'left',
          value: 'left',
        },
        {
          label: 'center',
          value: 'center',
        },
        {
          label: 'right',
          value: 'right',
        },
      ],
    },
    width: 180,
  },
  {
    title: '宽度',
    dataIndex: 'width',
    edit: true,
    editRule: true,
    editComponent: 'InputNumber',
    editComponentProps: () => {
      return {
        max: 1500,
        min: 0,
      };
    },
    width: 180,
  },
  {
    title: '是否可拖动列',
    dataIndex: 'resizable',
    edit: true,
    editComponent: 'Checkbox',
    editValueMap: (value) => {
      return value ? '是' : '否';
    },
    width: 180,
  },
];
