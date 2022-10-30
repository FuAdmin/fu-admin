<template>
  <div>
    <BasicTable @register="registerTable">
      <template #tableTitle>
        <a-button type="primary" @click="handleCreate"> {{ t('common.addText') }} </a-button>
      </template>
      <template #bodyCell="{ column, record }">
        <template v-if="column.key === 'action'">
          <TableAction
            :actions="[
              {
                type: 'button',
                icon: 'clarity:note-edit-line',
                color: 'primary',
                onClick: handleEdit.bind(null, record),
              },
              {
                icon: 'ant-design:delete-outlined',
                type: 'button',
                color: 'error',
                placement: 'left',
                popConfirm: {
                  title: t('common.delHintText'),
                  confirm: handleDelete.bind(null, record.id),
                },
              },
            ]"
          />
        </template>
      </template>
    </BasicTable>
    <ButtonDrawer @register="registerDrawer" @success="handleSuccess" />
  </div>
</template>
<script lang="ts">
  import { defineComponent } from 'vue';

  import { BasicTable, useTable, TableAction } from '/@/components/Table';

  import { useDrawer } from '/@/components/Drawer';
  import ButtonDrawer from './ButtonDrawer.vue';

  import { deleteItem, getList } from '/@/views/fuadmin/system/button/button.api';
  import { columns, searchFormSchema } from '/@/views/fuadmin/system/button/button.data';
  import { useI18n } from '/@/hooks/web/useI18n';

  export default defineComponent({
    name: 'ButtonManagement',
    components: { BasicTable, ButtonDrawer, TableAction },
    setup() {
      const { t } = useI18n();

      const [registerDrawer, { openDrawer }] = useDrawer();

      const [registerTable, { reload }] = useTable({
        api: getList,
        columns,
        formConfig: {
          labelWidth: 120,
          schemas: searchFormSchema,
        },
        useSearchForm: true,
        showTableSetting: true,
        tableSetting: { fullScreen: true },
        bordered: true,
        showIndexColumn: false,
        actionColumn: {
          width: 150,
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
        await reload();
      }

      function handleSuccess() {
        reload();
      }

      return {
        registerTable,
        registerDrawer,
        handleCreate,
        handleEdit,
        handleDelete,
        handleSuccess,
        t,
      };
    },
  });
</script>
