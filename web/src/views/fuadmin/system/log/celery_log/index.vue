<template>
  <div>
    <BasicTable @register="registerTable">
      <template #bodyCell="{ column, record }">
        <template v-if="column.key === 'action'">
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
  import { useI18n } from '/@/hooks/web/useI18n';

  export default defineComponent({
    name: 'CeleryLogManagement',
    components: { BasicTable, Drawer, TableAction },
    setup() {
      const { t } = useI18n();
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
          title: t('common.operationText'),
          dataIndex: 'action',
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
        message.success(t('common.successText'));
        await reload();
      }

      function handleSuccess() {
        message.success(t('common.successText'));
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
