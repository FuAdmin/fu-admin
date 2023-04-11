<template>
  <BasicDrawer v-bind="$attrs" @register="registerDrawerMenu" :title="getTitle" width="50%">
    <Tabs v-model:activeKey="activeKey" type="card">
      <TabPane key="1" tab="菜单按钮">
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
      </TabPane>
      <TabPane key="2" tab="列表字段">
        <BasicTable @register="registerColumnTable">
          <template #tableTitle>
            <Space style="height: 40px">
              <a-button type="primary" @click="handleColumnCreate">
                {{ t('common.addText') }}
              </a-button>
              <a-button
                type="error"
                v-auth="['demo:delete']"
                preIcon="ant-design:delete-outlined"
                @click="handleColumnBulkDelete"
              >
                {{ t('common.delText') }}
              </a-button>
              <a-button type="success" @click="handleQuickImport">
                {{ t('common.quickImport') }}
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
                    onClick: handleColumnEdit.bind(null, record),
                  },
                  {
                    icon: 'ant-design:delete-outlined',
                    type: 'button',
                    color: 'error',
                    placement: 'left',
                    popConfirm: {
                      title: t('common.delHintText'),
                      confirm: handleColumnDelete.bind(null, record.id),
                    },
                  },
                ]"
              />
            </template>
          </template>
        </BasicTable>
      </TabPane>
    </Tabs>
    <MenuButtonDrawer @register="registerDrawer" @success="handleSuccess" />
    <MenuColumnFieldDrawer @register="registerColumnDrawer" @success="handleColumnSuccess" />
    <MenuColumnQuickDrawer @register="registerQuickDrawer" @success="handleQuickSuccess" />
  </BasicDrawer>
</template>
<script lang="ts">
  import { defineComponent, ref, unref } from 'vue';

  import { BasicTable, useTable, TableAction } from '/@/components/Table';
  import { Tabs, TabPane, Space, message } from 'ant-design-vue';
  import { BasicDrawer, useDrawer, useDrawerInner } from '/@/components/Drawer';
  import { deleteItem, getList } from './menu_button.api';
  import {
    deleteItem as deleteColumnItem,
    getList as getColumnList,
  } from './menu_column_field.api';

  import { columns } from './menu_button.data';

  import { columns as columnColumns } from './menu_column_field.data';

  import MenuButtonDrawer from '/@/views/fuadmin/system/menu/add_button/MenuButtonDrawer.vue';
  import { useI18n } from '/@/hooks/web/useI18n';
  import MenuColumnFieldDrawer from '/@/views/fuadmin/system/menu/add_button/MenuColumnFieldDrawer.vue';
  import MenuColumnQuickDrawer from '/@/views/fuadmin/system/menu/add_button/MenuColumnQuickDrawer.vue';
  import { useMessage } from '/@/hooks/web/useMessage';

  export default defineComponent({
    name: 'AddMenuButton',
    components: {
      MenuColumnQuickDrawer,
      MenuColumnFieldDrawer,
      BasicTable,
      MenuButtonDrawer,
      BasicDrawer,
      TableAction,
      Tabs,
      TabPane,
      Space,
    },
    setup() {
      const { t } = useI18n();
      const activeKey = ref('1');
      const [registerDrawer, { openDrawer }] = useDrawer();
      const [registerColumnDrawer, { openDrawer: openColumnDrawer }] = useDrawer();
      const [registerQuickDrawer, { openDrawer: openQuickDrawer }] = useDrawer();
      const { createConfirm } = useMessage();

      const menuId = ref(0);
      const path = ref();
      const [registerDrawerMenu] = useDrawerInner(async (data) => {
        menuId.value = data.id;
        path.value = data.path;
        await reload();
      });
      const getTitle = '添加按钮和列';

      const [registerTable, { reload }] = useTable({
        api: getList,
        columns,
        showTableSetting: true,
        bordered: true,
        showIndexColumn: false,
        searchInfo: {
          menu_id: menuId,
        },
        actionColumn: {
          width: 50,
          title: t('common.operationText'),
          dataIndex: 'action',
          fixed: 'right',
        },
      });

      const [registerColumnTable, { reload: reloadColumn, getSelectRows }] = useTable({
        api: getColumnList,
        columns: columnColumns,
        showTableSetting: true,
        bordered: true,
        showIndexColumn: true,
        searchInfo: {
          menu_id: menuId,
        },
        rowSelection: {
          type: 'checkbox',
        },
        actionColumn: {
          width: 50,
          title: t('common.operationText'),
          dataIndex: 'action',
          fixed: 'right',
        },
      });

      function handleCreate() {
        openDrawer(true, {
          isUpdate: false,
          menuId: unref(menuId),
        });
      }

      function handleEdit(record: Recordable) {
        openDrawer(true, {
          record,
          isUpdate: true,
          menuId: unref(menuId),
        });
      }

      async function handleDelete(id: number) {
        await deleteItem(id);
        await reload();
      }

      function handleSuccess() {
        reload();
      }

      function handleColumnCreate() {
        openColumnDrawer(true, {
          isUpdate: false,
          menuId: unref(menuId),
        });
      }

      function handleColumnEdit(record: Recordable) {
        openColumnDrawer(true, {
          record,
          isUpdate: true,
          menuId: unref(menuId),
        });
      }

      async function handleColumnDelete(id: number) {
        await deleteColumnItem(id);
        await reloadColumn();
      }

      async function handleColumnBulkDelete() {
        if (getSelectRows().length == 0) {
          message.warning(t('common.batchDelHintText'));
        } else {
          createConfirm({
            iconType: 'warning',
            title: t('common.hintText'),
            content: t('common.delHintText'),
            async onOk() {
              for (const item of getSelectRows()) {
                await handleColumnDelete(item.id);
              }
              message.success(t('common.successText'));
            },
          });
        }
        await reloadColumn();
      }

      function handleColumnSuccess() {
        reloadColumn();
      }

      function handleQuickImport() {
        openQuickDrawer(true, {
          path: unref(path),
          menuId: unref(menuId),
        });
      }

      function handleQuickSuccess() {
        reloadColumn();
      }

      return {
        registerTable,
        registerDrawer,
        handleCreate,
        handleEdit,
        handleDelete,
        handleSuccess,
        handleColumnCreate,
        handleColumnEdit,
        handleColumnDelete,
        handleColumnSuccess,
        registerDrawerMenu,
        registerColumnTable,
        registerColumnDrawer,
        handleQuickImport,
        handleQuickSuccess,
        registerQuickDrawer,
        getTitle,
        activeKey,
        handleColumnBulkDelete,
        t,
      };
    },
  });
</script>
