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
            新增
          </a-button>
          <a-button
            type="error"
            v-auth="['post:delete']"
            preIcon="ant-design:delete-outlined"
            @click="handleBulkDelete"
          >
            删除
          </a-button>
        </Space>
      </template>
      <template #action="{ record }">
        <TableAction
          :actions="[
            {
              type: 'button',
              icon: 'clarity:note-edit-line',
              color: 'primary',
              tooltip: '编辑',
              onClick: handleEdit.bind(null, record),
              auth: ['dict:update'],
            },
            {
              icon: 'ant-design:delete-outlined',
              type: 'button',
              color: 'error',
              tooltip: '删除',
              placement: 'left',
              popConfirm: {
                title: '是否确认删除',
                confirm: handleDelete.bind(null, record.id),
              },
              auth: ['dict:delete'],
            },
            {
              type: 'button',
              color: 'warning',
              tooltip: '字典配置',
              icon: 'ant-design:plus-square-outlined',
              onClick: addDictItem.bind(null, record.id),
              auth: ['dict:update'],
            },
          ]"
        />
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

  export default defineComponent({
    name: 'DataDict',
    components: { BasicTable, DictDrawer, TableAction, AddDictItem, Space },
    setup() {
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

      function addDictItem(id: number) {
        openAddDictItemDrawer(true, {
          id,
        });
      }

      async function handleDelete(id: number) {
        await deleteItem(id);
        message.success('删除成功');
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
      };
    },
  });
</script>
