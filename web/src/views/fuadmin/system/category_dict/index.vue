<template>
  <div>
    <BasicTable @register="registerTable" @fetch-success="onFetchSuccess">
      <template #tableTitle>
        <Space style="height: 40px">
          <a-button
            type="primary"
            v-auth="['category:add']"
            preIcon="ant-design:plus-outlined"
            @click="handleCreate"
          >
            新增
          </a-button>
          <a-button
            type="error"
            v-auth="['category:delete']"
            preIcon="ant-design:delete-outlined"
            @click="handleBulkDelete"
          >
            删除
          </a-button>
        </Space>
      </template>
      <template #toolbar>
        <a-button type="primary" @click="expandAll">展开</a-button>
        <a-button type="primary" @click="collapseAll">折叠</a-button>
      </template>
      <template #action="{ record }">
        <TableAction
          :actions="[
            {
              type: 'button',
              color: 'primary',
              auth: ['category:update'],
              icon: 'clarity:note-edit-line',
              onClick: handleEdit.bind(null, record),
            },
            {
              type: 'button',
              color: 'error',
              auth: ['category:delete'],
              icon: 'ant-design:delete-outlined',
              placement: 'left',
              popConfirm: {
                title: '是否确认删除',
                confirm: handleDelete.bind(null, record.id),
              },
            },
          ]"
        />
      </template>
    </BasicTable>
    <CategoryDictDrawer @register="registerDrawer" @success="handleSuccess" />
  </div>
</template>
<script lang="ts">
  import { defineComponent, nextTick } from 'vue';

  import { BasicTable, useTable, TableAction } from '/@/components/Table';

  import { useDrawer } from '/@/components/Drawer';
  import CategoryDictDrawer from './CategoryDictDrawer.vue';

  import { columns, searchFormSchema } from './category_dict.data';
  import { getList, deleteItem } from './category_dict.api';
  import { message, Space } from 'ant-design-vue';
  import { useMessage } from '/@/hooks/web/useMessage';
  export default defineComponent({
    name: 'CategoryDictManagement',
    components: { BasicTable, CategoryDictDrawer, TableAction, Space },
    setup() {
      const [registerDrawer, { openDrawer }] = useDrawer();
      const [registerTable, { reload, expandAll, getSelectRows, collapseAll }] = useTable({
        title: '',
        api: getList,
        columns,
        formConfig: {
          labelWidth: 80,
          schemas: searchFormSchema,
        },
        rowSelection: {
          type: 'checkbox',
        },
        isTreeTable: true,
        pagination: false,
        striped: false,
        useSearchForm: true,
        showTableSetting: true,
        bordered: true,
        showIndexColumn: false,
        canResize: false,
        tableSetting: { fullScreen: true },
        actionColumn: {
          align: 'left',
          width: 150,
          title: '操作',
          dataIndex: 'action',
          slots: { customRender: 'action' },
          fixed: undefined,
        },
      });
      const { createConfirm } = useMessage();
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

      function handleBulkDelete() {
        if (getSelectRows().length == 0) {
          message.warning('请选择一个选项');
        } else {
          createConfirm({
            iconType: 'warning',
            title: '提示',
            content: '是否确认删除？',
            async onOk() {
              for (const item of getSelectRows()) {
                await deleteItem(item.id);
              }
              message.success('删除成功');
              await reload();
            },
          });
        }
      }

      function handleSuccess() {
        reload();
      }

      function onFetchSuccess() {
        // 演示默认展开所有表项
        nextTick(expandAll);
      }

      return {
        registerTable,
        registerDrawer,
        handleCreate,
        handleEdit,
        handleDelete,
        handleSuccess,
        onFetchSuccess,
        expandAll,
        collapseAll,
        handleBulkDelete,
      };
    },
  });
</script>
