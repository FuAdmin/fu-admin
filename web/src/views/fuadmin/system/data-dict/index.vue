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
                color: 'primary',
                tooltip: t('common.updateText'),
                onClick: handleEdit.bind(null, record),
                auth: ['dict:update'],
              },
              {
                icon: 'ant-design:delete-outlined',
                type: 'button',
                color: 'error',
                tooltip: t('common.delText'),
                placement: 'left',
                popConfirm: {
                  title: t('common.delHintText'),
                  confirm: handleDelete.bind(null, record.id),
                },
                auth: ['dict:delete'],
              },
              {
                type: 'button',
                color: 'warning',
                tooltip: t('common.dictConfigText'),
                icon: 'ant-design:plus-square-outlined',
                onClick: addDictItem.bind(null, record.id),
                auth: ['dict:update'],
              },
            ]"
          />
        </template>
      </template>
    </BasicTable>
    <DictDrawer @register="registerDrawer" @success="handleSuccess" />
    <AddDictItem @register="registerAddDictItemDrawer" />
  </div>
</template>
<script lang="ts">
  import { defineComponent } from 'vue';

  import { BasicTable, useTable, TableAction } from '/@/components/Table';

  import { useDrawer } from '/@/components/Drawer';
  import DictDrawer from './DictDrawer.vue';
  import AddDictItem from './dict_item/index.vue';

  import { deleteItem, getList } from './dict.api';
  import { columns, searchFormSchema } from './dict.data';
  import { message, Space } from 'ant-design-vue';
  import { useMessage } from '/@/hooks/web/useMessage';
  import { useI18n } from '/@/hooks/web/useI18n';

  export default defineComponent({
    name: 'DataDict',
    components: { BasicTable, DictDrawer, TableAction, AddDictItem, Space },
    setup() {
      const { t } = useI18n();
      const [registerDrawer, { openDrawer }] = useDrawer();
      const [registerAddDictItemDrawer, { openDrawer: openAddDictItemDrawer }] = useDrawer();
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

      function addDictItem(id: number) {
        openAddDictItemDrawer(true, {
          id,
        });
      }

      async function handleDelete(id: number) {
        await deleteItem(id);
        message.success(t('common.successText'));
        await reload();
      }

      function handleBulkDelete() {
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
        registerAddDictItemDrawer,
        handleCreate,
        handleEdit,
        handleDelete,
        handleSuccess,
        addDictItem,
        handleBulkDelete,
        t,
      };
    },
  });
</script>
