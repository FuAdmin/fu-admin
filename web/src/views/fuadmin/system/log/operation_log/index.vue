<template>
  <div>
    <BasicTable @register="registerTable">
      <template #action="{ record }">
        <TableAction
          :actions="[
            {
              type: 'button',
              icon: 'bi:eye',
              color: 'success',
              auth: ['post:update'],
              onClick: handleEdit.bind(null, record),
            },
          ]"
        />
      </template>
    </BasicTable>
    <Drawer @register="registerDrawer" @success="handleSuccess" />
  </div>
</template>
<script lang="ts">
  import { defineComponent } from 'vue';

  import { BasicTable, useTable, TableAction } from '/@/components/Table';
  import { usePermission } from '/@/hooks/web/usePermission';

  import { useDrawer } from '/@/components/Drawer';
  import Drawer from './Drawer.vue';

  import { deleteItem, getList } from './api';
  import { columns, searchFormSchema } from './data';
  import { message } from 'ant-design-vue';

  export default defineComponent({
    name: 'OperationLogManagement',
    components: { BasicTable, Drawer, TableAction },
    setup() {
      const [registerDrawer, { openDrawer }] = useDrawer();
      // const { createMessage } = useMessage();
      const { hasPermission } = usePermission();
      const [registerTable, { reload }] = useTable({
        api: getList,
        columns,
        formConfig: {
          labelWidth: 80,
          schemas: searchFormSchema,
        },
        useSearchForm: true,
        showTableSetting: true,
        tableSetting: { fullScreen: true },
        bordered: true,
        showIndexColumn: false,
        actionColumn: {
          width: 80,
          title: '操作',
          dataIndex: 'action',
          slots: { customRender: 'action' },
          fixed: undefined,
        },
      });

      function handleCreate() {
        openDrawer(true, {
          isUpdate: false,
        });
      }

      function handleEdit(record: Recordable) {
        openDrawer(true, {
          record,
          isUpdate: true,
        });
      }

      async function handleDelete(id: number) {
        await deleteItem(id);
        message.success('删除成功');
        await reload();
      }

      function handleSuccess() {
        message.success('请求成功');
        reload();
      }

      return {
        registerTable,
        registerDrawer,
        handleCreate,
        handleEdit,
        handleDelete,
        handleSuccess,
        hasPermission,
      };
    },
  });
</script>
