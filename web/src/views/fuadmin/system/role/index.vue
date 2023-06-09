<template>
  <div>
    <BasicTable @register="registerTable">
      <template #tableTitle>
        <Space style="height: 40px">
          <a-button
            type="primary"
            v-auth="['post:add']"
            preIcon="ant-design:plus-outlined"
            @click="handleCreate"
          >
            {{ t('common.addText') }}
          </a-button>
          <a-button
            type="error"
            v-auth="['post:delete']"
            preIcon="ant-design:delete-outlined"
            @click="handleBulkDelete"
          >
            {{ t('common.delText') }}
          </a-button>
        </Space>
      </template>

      <template #bodyCell="{ column, record }">
        <template v-if="column.key === 'action'">
          <TableAction
            :actions="[
              {
                type: 'button',
                icon: 'clarity:note-edit-line',
                auth: ['role:update'],
                color: 'primary',
                onClick: handleEdit.bind(null, record),
              },
              {
                icon: 'ant-design:delete-outlined',
                type: 'button',
                color: 'error',
                auth: ['role:delete'],
                placement: 'left',
                popConfirm: {
                  title: t('common.delHintText'),
                  confirm: handleDelete.bind(null, record.id),
                },
              },
              {
                type: 'button',
                color: 'warning',
                auth: ['role:update'],
                onClick: handlePermission.bind(null, record),
                label: t('common.role.permissionMng')
              },
            ]"
          />
        </template>
      </template>
    </BasicTable>
    <RoleDrawer @register="registerDrawer" @success="handleSuccess" />
    <PermissionDrawer @register="registerPermissionDrawer" @success="handleSuccess" />
  </div>
</template>
<script lang="ts">
  import { defineComponent } from 'vue';

  import { BasicTable, useTable, TableAction } from '/@/components/Table';

  import { useDrawer } from '/@/components/Drawer';
  import RoleDrawer from './RoleDrawer.vue';
  import PermissionDrawer from './PermissionDrawer/index.vue';

  import { columns, searchFormSchema } from './role.data';
  import { getList, deleteItem } from '/@/views/fuadmin/system/role/role.api';
  import { message, Space } from 'ant-design-vue';
  import { useMessage } from '/@/hooks/web/useMessage';
  import { useI18n } from '/@/hooks/web/useI18n';

  export default defineComponent({
    name: 'RoleManagement',
    components: { BasicTable, RoleDrawer, TableAction, PermissionDrawer, Space },
    setup() {
      const { t } = useI18n();

      const [registerDrawer, { openDrawer }] = useDrawer();
      const [registerPermissionDrawer, { openDrawer: openPermissionDrawer }] = useDrawer();
      const { createConfirm } = useMessage();
      const [registerTable, { reload, getSelectRows }] = useTable({
        api: getList,
        columns,
        formConfig: {
          labelWidth: 80,
          schemas: searchFormSchema,
        },
        rowSelection: {
          type: 'checkbox',
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

      function handlePermission(record: Recordable) {
        openPermissionDrawer(true, record);
      }

      async function handleDelete(id: number) {
        await deleteItem(id);
        message.success(t('common.successText'));
        await reload();
      }

      async function handleBulkDelete() {
        if (getSelectRows().length == 0) {
          message.warning(t('common.batchDelHintText'));
        } else {
          createConfirm({
            iconType: 'warning',
            title: t('common.hintText'),
            content: t('common.delHintText'),
            async onOk() {
              for (const item of getSelectRows()) {
                await deleteItem(item.id);
              }
              message.success(t('common.successText'));
              await reload();
            },
          });
        }
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
        handlePermission,
        registerPermissionDrawer,
        handleBulkDelete,
        t,
      };
    },
  });
</script>
