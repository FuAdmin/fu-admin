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
    width: 180,
  },
  {
    title: '是否多选',
    dataIndex: 'is_check',
    width: 180,
  },
];
